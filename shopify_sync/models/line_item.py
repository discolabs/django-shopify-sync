from django.db import models
import shopify
import jsonfield

from .base import ShopifyResourceModel


class LineItem(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.LineItem

    fulfillable_quantity = models.IntegerField()
    fulfillment_service = models.CharField(max_length = 32)
    fulfillment_status = models.CharField(max_length = 32, null = True)
    grams = models.DecimalField(max_digits = 10, decimal_places = 2)
    order = models.ForeignKey('shopify_sync.Order')
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    product = models.ForeignKey('shopify_sync.Product')
    quantity = models.IntegerField()
    requires_shipping = models.BooleanField(default = True)
    sku = models.CharField(max_length = 256)
    title = models.CharField(max_length = 256)
    variant = models.ForeignKey('shopify_sync.Variant')
    variant_title = models.CharField(max_length = 256)
    vendor = models.CharField(max_length = 64)
    name = models.CharField(max_length = 256)
    gift_card = models.BooleanField(default = False)
    taxable = models.BooleanField(default = False)
    tax_lines = jsonfield.JSONField(default = [])

    class Meta:
        app_label = 'shopify_sync'
