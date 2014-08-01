from .base import ShopifyDatedResourceModel
from django.db import models
import shopify


class Image(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.Image

    position = models.IntegerField(default = 1)
    product = models.ForeignKey('Product')
    src = models.URLField()

    def __unicode__(self):
        return self.src

    class Meta:
        app_label = 'shopify_sync'