from .base import ShopifyDatedResourceModel
from django.db import models
from jsonfield import JSONField
import shopify


class CustomCollection(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.CustomCollection

    body_html = models.TextField()
    handle = models.CharField(max_length = 255)
    image = JSONField(null = True)
    published = models.BooleanField(default = True)
    published_at = models.DateTimeField(null = True)
    published_scope = models.CharField(max_length = 16)
    sort_order = models.CharField(max_length = 16)
    template_suffix = models.CharField(max_length = 32, null = True)
    title = models.CharField(max_length = 255)

    class Meta:
        abstract = True