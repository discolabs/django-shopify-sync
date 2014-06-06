from .base import ShopifyDatedResourceModel
from django.db import models
import shopify


class Product(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.Product

    body_html = models.TextField()
    handle = models.CharField(max_length = 255, db_index = True)
    product_type = models.CharField(max_length = 255, db_index = True)
    published_at = models.DateTimeField(null = True)
    published_scope = models.CharField(max_length = 64)
    tags = models.CharField(max_length = 255)
    template_suffix = models.CharField(max_length = 255, null = True)
    title = models.CharField(max_length = 255, db_index = True)
    vendor = models.CharField(max_length = 255, db_index = True)

    class Meta:
        app_label = 'shopify_sync'