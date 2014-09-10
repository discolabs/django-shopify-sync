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
        instance, created = self.update_or_create(user, id = shopify_resource.id, defaults = self.model.get_defaults(shopify_resource))
        return instance

    def sync_many(self, user, shopify_resources):
        """
        Given an array of Shopify resource objects, synchronise all of them locally so that we have up-to-date versions
        in the local database, Returns an array of the created or updated local models.
        """
        instances = []
        for shopify_resource in shopify_resources:
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
        return [field.name for field in cls._meta.concrete_fields if field.name not in default_fields_excluded]

    @classmethod
    def get_default_fields_excluded(cls):
        """
        Get a list of field names to be excluded when copying directly from a Shopify resource model and building
        a defaults hash.
        """
        return []

    @classmethod
    def shopify_resource_from_json(cls, json):
        instance = cls.shopify_resource_class()
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
