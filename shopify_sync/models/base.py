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
    def sync_all_for_user(cls, user):
        with user.session:
            shopify_resources = cls.shopify_resource.find()
        for shopify_resource in shopify_resources:
            resource = cls(user, shopify_resource = shopify_resource)
            resource.save()

    class Meta:
        abstract = True