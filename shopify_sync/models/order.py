from django.db import models
import shopify
import jsonfield

from .base import ShopifyDatedResourceModel
from .line_item import LineItem


class Order(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.Order

    billing_address = jsonfield.JSONField()
    browser_ip = models.IPAddressField(null = True)
    buyer_accepts_marketing = models.BooleanField(default = False)
    cancel_reason = models.CharField(max_length = 32, null = True)
    cancelled_at = models.DateTimeField(null = True)
    cart_token = models.CharField(max_length = 32, null = True)
    client_details = jsonfield.JSONField()
    closed_at = models.DateTimeField(null = True)
    currency = models.CharField(max_length = 3)
    customer = models.ForeignKey('shopify_sync.Customer')
    discount_codes = jsonfield.JSONField(default = [])
    email = models.EmailField()
    financial_status = models.CharField(max_length = 32)
    fulfillment_status = models.CharField(max_length = 32, null = True)
    tags = models.TextField()
    landing_site = models.URLField(null = True)
    name = models.CharField(max_length = 32)
    note = models.TextField()
    note_attributes = jsonfield.JSONField()
    number = models.IntegerField()
    order_number = models.IntegerField()
    processed_at = models.DateTimeField()
    processing_method = models.CharField(max_length = 32)
    referring_site = models.URLField(null = True)
    shipping_address = jsonfield.JSONField(null = True)
    shipping_lines = jsonfield.JSONField(default = [])
    source_name = models.CharField(max_length = 32)
    tax_lines = jsonfield.JSONField(default = [])
    taxes_included = models.BooleanField(default = True)
    token = models.CharField(max_length = 32)
    total_discounts = models.DecimalField(max_digits = 10, decimal_places = 2)
    total_line_items_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    total_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    total_tax = models.DecimalField(max_digits = 10, decimal_places = 2)
    total_weight = models.DecimalField(max_digits = 10, decimal_places = 2)

    class Meta:
        app_label = 'shopify_sync'

    @property
    def fulfillments(self):
        return []

    @property
    def line_items(self):
        return LineItem.objects.filter_for_user(self.user, order = self)

    @property
    def refund(self):
        return []

    def __unicode__(self):
        return unicode(self.name)
