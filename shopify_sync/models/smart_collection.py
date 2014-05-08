from .base import ShopifyResourceModel
from django.db import models
import shopify


class SmartCollection(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.SmartCollection

    handle = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    published = models.BooleanField(default = True)

    class Meta:
        abstract = True