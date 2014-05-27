from .base import ShopifyDatedResourceModel
from django.db import models
import shopify


class ScriptTag(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.ScriptTag

    event = models.CharField(max_length = 16)
    src = models.URLField()

    class Meta:
        abstract = True