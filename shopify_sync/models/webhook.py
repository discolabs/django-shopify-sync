from .base import ShopifyResourceModel
from django.db import models
from jsonfield import JSONField
import shopify


class Webhook(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.Webhook

    address = models.URLField()
    created_at = models.DateTimeField()
    fields = JSONField()
    format = models.CharField(max_length = 4)
    metafield_namespaces = JSONField()
    topic = models.CharField(max_length = 64)
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True