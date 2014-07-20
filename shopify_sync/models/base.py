import six
from django.db import models, transaction

from owned_models.models import UserOwnedModel, UserOwnedModelManager


class ShopifyResourceModelManager(UserOwnedModelManager):

    def create_for_user(self, user, **kwargs):
        """Create a new Shopify resource, then synchronise and save it to a local model."""

        # Instantiate the new model and get its Shopify resource equivalent.
        local_model = self.model(user = user, **kwargs)

        # Try to save to Shopify.
        with user.session:
            shopify_resource = local_model.as_shopify_resource()
            if not shopify_resource.save():
                raise Exception('Save failed.')

        return self.sync_for_user(user, shopify_resource)

    def sync_for_user(self, user, shopify_resource):
        """Create a local model for the given Shopify resource. If it already exists, update it."""

        # Get a 'cleaned' hash from the shopify resource that only contains model fields we're aware of.
        # Defends against the Shopify API returning additional fields.
        cleaned_defaults = dict((field, value) for field, value in six.iteritems(shopify_resource.attributes) if field in self.model.get_field_names())

        # Try to get an existing version of the model. If it doesn't exist, create it.
        try:
            local_model = self.get_for_user(user, id = shopify_resource.id)
        except self.model.DoesNotExist:
            local_model, created = self.get_or_create_for_user(user, id = shopify_resource.id, defaults = cleaned_defaults)
            if created:
                return local_model

        # Copy attribute values from the cleaned defaults.
        for field, value in six.iteritems(cleaned_defaults):
            setattr(local_model, field, value)

        # Save the updates to the database and return the updated model.
        with transaction.atomic(using = self.db, savepoint = False):
            local_model.save(using = self.db)
        return local_model

    def sync_all_for_user(self, user, **kwargs):
        """Fetch and synchronise all models of this resource type. Optionally use **kwargs to filter."""
        local_models = []
        with user.session:
            shopify_resources = self.model.shopify_resource_class.find(**kwargs)
        for shopify_resource in shopify_resources:
            local_models.append(self.sync_for_user(user, shopify_resource))
        return local_models

    class Meta:
        abstract = True


class ShopifyResourceModel(UserOwnedModel):

    shopify_resource_class = None

    objects = ShopifyResourceModelManager()

    def from_shopify_resource(self, shopify_resource):
        """Update this model from the given Shopify resource."""
        for attribute in shopify_resource.attributes:
                if hasattr(self, attribute):
                    setattr(self, attribute, getattr(shopify_resource, attribute))

    def as_shopify_resource(self):
        """Return this model as a Shopify resource."""
        attributes = dict((field_name, getattr(self, field_name)) for field_name in self.get_field_names())
        return self.shopify_resource_class(attributes)

    @classmethod
    def get_field_names(cls):
        excluded_fields = ['user']
        return [field.name for field in cls._meta.concrete_fields if field.name not in excluded_fields]

    class Meta:
        abstract = True


class ShopifyDatedResourceModel(ShopifyResourceModel):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True