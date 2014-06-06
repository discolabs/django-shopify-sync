from .base import ShopifyDatedResourceModel
from ..encoders import ShopifyDjangoJSONEncoder
from django.db import models
from jsonfield import JSONField
import shopify


class SmartCollection(ShopifyDatedResourceModel):
    shopify_resource_class = shopify.resources.SmartCollection

    body_html = models.TextField(null = True)
    handle = models.CharField(max_length = 255)
    image = JSONField(null = True, dump_kwargs = {'cls': ShopifyDjangoJSONEncoder})
    published_at = models.DateTimeField(null = True)
    published_scope = models.CharField(max_length = 16, default = 'global')
    rules = JSONField(dump_kwargs = {'cls': ShopifyDjangoJSONEncoder})
    disjunctive = models.BooleanField(default = False)
    sort_order = models.CharField(max_length = 16)
    template_suffix = models.CharField(max_length = 32, null = True)
    title = models.CharField(max_length = 255)

    class Meta:
        app_label = 'shopify_sync'