from owned_models.models import UserOwnedModel, UserOwnedModelManager


class ShopifyResourceModelManager(UserOwnedModelManager):

    def create_for_user(self, user, shopify_resource = None):
        resource = self.model(user = user)
        if shopify_resource:
            for attribute in shopify_resource.attributes:
                if hasattr(resource, attribute):
                    setattr(resource, attribute, getattr(shopify_resource, attribute))

    def sync_for_user(self, user, **kwargs):
        with user.session:
            shopify_resources = self.model.shopify_resource_class.find(**kwargs)
        for shopify_resource in shopify_resources:
            self.create_for_user(user, shopify_resource = shopify_resource).save()

    class Meta:
        abstract = True


class ShopifyResourceModel(UserOwnedModel):

    shopify_resource_class = None

    objects = ShopifyResourceModelManager()

    class Meta:
        abstract = True