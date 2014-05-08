from owned_models.models import UserOwnedModel


class ShopifyResourceModel(UserOwnedModel):
    shopify_resource_class = None

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        shopify_resource = kwargs.pop('shopify_resource', None)
        super(ShopifyResourceModel, self).__init__(*args, **kwargs)
        if shopify_resource:
            for attribute in shopify_resource.attributes:
                if hasattr(self, attribute):
                    setattr(self, attribute, getattr(shopify_resource, attribute))
        if not self.user:
            self.user = user

    @classmethod
    def sync_for_user(cls, user, **kwargs):
        with user.session:
            shopify_resources = cls.shopify_resource_class.find(**kwargs)
        for shopify_resource in shopify_resources:
            cls(user = user, shopify_resource = shopify_resource).save()

    class Meta:
        abstract = True