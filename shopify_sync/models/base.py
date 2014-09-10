import six, json
from django.db import models, transaction

from owned_models.models import UserOwnedModel, UserOwnedManager


def get_shopify_sync_model(model):
    if isinstance(model, basestring):
        model = models.get_model('shopify_sync', model)
    return model


class ShopifyResourceModelManager(UserOwnedManager):

    def create(self, user, **kwargs):
        """
        Override the create() method of the UserOwnedManager.
        Creates the resource through an API call to Shopify, then syncs and saves locally.
        """
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

        # Synchronise any related model attributes first.
        # Related models are those that should be created before the main model we're synchronising with.
        for related_attribute, related_model in six.iteritems(self.model.shopify_related_attributes):
            related_model_instance = self._sync_related(user, related_attribute, related_model, shopify_resource)
            if related_model_instance is not None:
                setattr(shopify_resource, related_attribute + '_id', related_model_instance.id)

        # Synchronise the model itself.
        local_model = self._sync(user, shopify_resource)

        # Synchronise any child model attributes.
        # Child models are those that are 'attached' to the main model we're synchronising with.
        for child_attribute, child_model in six.iteritems(self.model.shopify_child_attributes):
            self._sync_children(user, child_attribute, child_model, shopify_resource)

        return local_model

    def _sync(self, user, shopify_resource):
        # Get a 'cleaned' hash from the shopify resource that only contains model fields we're aware of.
        cleaned_defaults = self.model.get_cleaned_defaults(shopify_resource)

        # Try to get an existing version of the model. If it doesn't exist, create it.
        try:
            local_model = self.get_for_user(user, id = shopify_resource.id)
        except self.model.DoesNotExist:
            local_model, created = self.get_or_create_for_user(user, id = shopify_resource.id, defaults = cleaned_defaults)
            if created:
                return local_model

        # Update the local model with the cleaned Shopify resource attributes.
        for field, value in six.iteritems(cleaned_defaults):
            setattr(local_model, field, value)

        # Save the updates to the database.
        with transaction.atomic(using = self.db, savepoint = False):
            local_model.save(using = self.db)

        # Return the updated model.
        return local_model

    def _sync_related(self, user, related_attribute, related_model, shopify_resource):
        # Ensure the related model is a class instance.
        related_model = get_shopify_sync_model(related_model)

        # Get the related Shopify resource from the passed Shopify model.
        shopify_related_resource = getattr(shopify_resource, related_attribute)

        if shopify_resource is None:
            return None

        # Perform a synchronisation with that related model, if it existed on the passed Shopify model.
        return related_model.objects.sync_for_user(user, shopify_related_resource)

    def _sync_children(self, user, child_attribute, child_model, shopify_resource):
        # Ensure the child model is a class instance.
        child_model = get_shopify_sync_model(child_model)

        # Get the child Shopify resources from the passed Shopify model.
        shopify_child_resources = getattr(shopify_resource, child_attribute, [])

        # Perform a synchronisation for each child model found.
        for shopify_child_resource in shopify_child_resources:
            child_model.objects.sync_for_user(user, shopify_child_resource)

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
    shopify_parent_field = None
    shopify_related_attributes = {}
    shopify_child_attributes = {}

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
    def get_cleaned_defaults(cls, shopify_resource):
        cleaned_defaults = {}

        for field, value in six.iteritems(shopify_resource.attributes):
            if field not in cls.get_field_names():
                continue

            if hasattr(value, 'attributes'):
                value = dict(value.attributes)

            if isinstance(value, list):
                new_list = []
                for list_value in value:
                    if hasattr(list_value, 'attributes'):
                        list_value = dict(list_value.attributes)
                    new_list.append(list_value)
                value = new_list

            cleaned_defaults[field] = value

        # Add related model id fields if present.
        for related_attribute in cls.shopify_related_attributes:
            related_id_attribute = related_attribute + '_id'
            if hasattr(shopify_resource, related_id_attribute):
                cleaned_defaults[related_id_attribute] = getattr(shopify_resource, related_id_attribute)

        # Add the parent field if present.
        if cls.shopify_parent_field is not None:
            cleaned_defaults[cls.shopify_parent_field] = shopify_resource._prefix_options[cls.shopify_parent_field]

        return cleaned_defaults

    @classmethod
    def get_field_names(cls):
        excluded_fields = ['user'] + [related_attribute for related_attribute in cls.shopify_related_attributes]
        return [field.name for field in cls._meta.concrete_fields if field.name not in excluded_fields]

    class Meta:
        abstract = True


class ShopifyDatedResourceModel(ShopifyResourceModel):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True
