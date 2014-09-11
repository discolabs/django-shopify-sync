from django.db import models

from owned_models.models import UserOwnedModel, UserOwnedManager


class ShopifyResourceManager(UserOwnedManager):
    """
    Base class for managing Shopify resource models.
    """

    def sync_one(self, user, shopify_resource):
        """
        Given a Shopify resource object, synchronise it locally so that we have an up-to-date version in the local
        database. Returns the created or updated local model.
        """
        # Synchronise instance.
        instance, created = self.update_or_create(user, id = shopify_resource.id, defaults = self.model.get_defaults(shopify_resource))

        # Synchronise any child fields.
        for child_field, child_model in self.model.get_child_fields().items():
            child_shopify_resources = getattr(shopify_resource, child_field)
            child_model.objects.sync_many(user, child_shopify_resources, parent_shopify_resource = shopify_resource)

        return instance

    def sync_many(self, user, shopify_resources, parent_shopify_resource = None):
        """
        Given an array of Shopify resource objects, synchronise all of them locally so that we have up-to-date versions
        in the local database, Returns an array of the created or updated local models.
        """
        instances = []
        for shopify_resource in shopify_resources:
            # If needed, ensure the parent ID is stored on the resource before synchronising it.
            if self.model.parent_field is not None and parent_shopify_resource is not None:
                setattr(shopify_resource, self.model.parent_field, getattr(parent_shopify_resource, 'id'))
            instance = self.sync_one(user, shopify_resource)
            instances.append(instance)
        return instances

    class Meta:
        abstract = True


class ShopifyResourceModel(UserOwnedModel):
    """
    Base class for local Model objects that are to be synchronised with Shopify.
    """

    shopify_resource_class = None
    parent_field = None
    child_fields = {}

    objects = ShopifyResourceManager()

    @classmethod
    def get_defaults(cls, shopify_resource):
        """
        Get a hash of attribute: values that can be used to update or create a local instance of the given Shopify
        resource.
        """
        defaults = {}
        for field in cls.get_default_fields():
            if hasattr(shopify_resource, field):
                defaults[field] = getattr(shopify_resource, field)
        return defaults

    @classmethod
    def get_default_fields(cls):
        """
        Get a list of field names that should be copied directly from a Shopify resource model when building the
        defaults hash.
        """
        default_fields_excluded = cls.get_default_fields_excluded()
        return cls.get_parent_fields() + [field.name for field in cls._meta.concrete_fields if field.name not in default_fields_excluded]

    @classmethod
    def get_default_fields_excluded(cls):
        """
        Get a list of field names to be excluded when copying directly from a Shopify resource model and building
        a defaults hash.
        """
        return ['user'] + cls.get_child_fields().keys()

    @classmethod
    def get_parent_fields(cls):
        if cls.parent_field is None:
            return []
        return [cls.parent_field]

    @classmethod
    def get_child_fields(cls):
        """
        Get a list of child fields for the current model, in a "hash" format with the name of the field as the key
        and the related child model as the value.
        """
        return cls.child_fields

    @classmethod
    def shopify_resource_from_json(cls, json):
        """
        Return an instance of the Shopify Resource model for this model, built recursively using the given JSON object.
        """
        instance = cls.shopify_resource_class()

        # Recursively instantiate any child attributes.
        for child_field, child_model in cls.get_child_fields().items():
            if child_field in json:
                json[child_field] = [child_model.shopify_resource_from_json(child_field_json) for child_field_json in json[child_field]]

        instance.attributes = json
        return instance

    class Meta:
        abstract = True


class ShopifyDatedResourceModel(ShopifyResourceModel):
    """
    Extends ShopifyResourceModel by adding two common fields for Shopify resources - `created_at` and `updated_at`.
    """

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True
