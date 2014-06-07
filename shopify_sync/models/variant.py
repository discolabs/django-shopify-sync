from .base import ShopifyDatedResourceModel
from django.db import models
import shopify


class Variant(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.Variant

    barcode = models.CharField(max_length = 255, null = True)
    compare_at_price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    fulfillment_service = models.CharField(max_length = 32, default = 'manual')
    grams = models.IntegerField()
    inventory_management = models.CharField(max_length = 32, default = 'blank')
    inventory_policy = models.CharField(max_length = 32, default = 'deny')
    inventory_quantity = models.IntegerField()
    option1 = models.CharField(max_length = 255, null = True)
    option2 = models.CharField(max_length = 255, null = True)
    option3 = models.CharField(max_length = 255, null = True)
    position = models.IntegerField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    product_id = models.IntegerField()
    requires_shipping = models.BooleanField(default = True)
    sku = models.CharField(max_length = 255, null = True)
    taxable = models.BooleanField(default = True)
    title = models.CharField(max_length = 255)

    class Meta:
        app_label = 'shopify_sync'