from django.db import models
import shopify

from .base import ShopifyDatedResourceModel


class Image(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.Image
    parent_field = 'product_id'

    position = models.IntegerField(default = 1)
    product = models.ForeignKey('shopify_sync.Product')
    src = models.URLField()

    class Meta:
        app_label = 'shopify_sync'

    def __unicode__(self):
        return self.src
