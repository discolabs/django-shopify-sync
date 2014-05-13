from .base import ShopifyResourceModel
from django.db import models
import shopify


class ScriptTag(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.ScriptTag

    created_at = models.DateTimeField()
    event = models.CharField(max_length = 16)
    src = models.URLField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True