from owned_models.models import UserOwnedModel


class ShopifyResourceModel(UserOwnedModel):
    shopify_resource = None

    def __init__(self, user, shopify_resource = None, *args, **kwargs):
        super(ShopifyResourceModel, self).__init__(*args, **kwargs)
        if shopify_resource:
            for attribute in shopify_resource.attributes:
                if hasattr(self, attribute):
                    setattr(self, attribute, getattr(shopify_resource, attribute))
        self.user = user

    @classmethod
    def sync_for_user(cls, user, **kwargs):
        with user.session:
            shopify_resources = cls.shopify_resource.find(**kwargs)
        for shopify_resource in shopify_resources:
            cls(user, shopify_resource = shopify_resource).save()

    class Meta:
        abstract = True