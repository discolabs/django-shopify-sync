from .base import ShopifyDatedResourceModel
from django.db import models
from jsonfield import JSONField
import shopify


class Webhook(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.Webhook

    topic = models.CharField(max_length = 64)
    address = models.URLField()
    format = models.CharField(max_length = 4)
    fields = JSONField(null = True)
    metafield_namespaces = JSONField(null = True)

    class Meta:
        abstract = True