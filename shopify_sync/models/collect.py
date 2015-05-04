from .base import ShopifyDatedResourceModel
from django.db import models
import shopify


class Collect(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.Collect

    collection_id = models.IntegerField()
    featured = models.BooleanField(default = False)
    position = models.IntegerField(null = True, default = 1)
    product_id = models.IntegerField()
    sort_value = models.CharField(max_length = 16, null = True)

    class Meta:
        app_label = 'shopify_sync'
