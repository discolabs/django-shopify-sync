from django.db import models
import shopify
from jsonfield import JSONField

from .base import ShopifyResourceModel
from ..encoders import ShopifyDjangoJSONEncoder, empty_list


class LineItem(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.LineItem
    parent_field = 'order_id'

    fulfillable_quantity = models.IntegerField()
    fulfillment_service = models.CharField(max_length = 32)
    fulfillment_status = models.CharField(max_length = 32, null = True)
    grams = models.DecimalField(max_digits = 10, decimal_places = 2)
    name = models.CharField(max_length = 256)
    order = models.ForeignKey('shopify_sync.Order')
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    product_id = models.IntegerField(null = True)
    product_exists = models.BooleanField(default = True)
    properties = JSONField(default = empty_list, dump_kwargs = {'cls': ShopifyDjangoJSONEncoder})
    quantity = models.IntegerField()
    requires_shipping = models.BooleanField(default = True)
    sku = models.CharField(max_length = 256)
    gift_card = models.BooleanField(default = False)
    taxable = models.BooleanField(default = False)
    tax_lines = JSONField(default = empty_list, dump_kwargs = {'cls': ShopifyDjangoJSONEncoder})
    title = models.CharField(max_length = 256)
    total_discount = models.DecimalField(max_digits = 10, decimal_places = 2)
    variant_id = models.IntegerField(null = True)
    variant_title = models.CharField(max_length = 256)
    vendor = models.CharField(max_length = 64)

    class Meta:
        app_label = 'shopify_sync'
