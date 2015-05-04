from django.db import models
import shopify

from .base import ShopifyResourceModel


class Option(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.Option
    parent_field = 'product_id'

    name = models.CharField(max_length = 255)
    position = models.IntegerField(null = True, default = 1)
    product = models.ForeignKey('shopify_sync.Product')

    class Meta:
        app_label = 'shopify_sync'
