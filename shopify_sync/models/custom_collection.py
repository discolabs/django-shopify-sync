from django.db import models
from jsonfield import JSONField
import shopify

from .base import ShopifyResourceModel
from .collect import Collect
from ..encoders import ShopifyDjangoJSONEncoder


class CustomCollection(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.CustomCollection

    body_html = models.TextField(null = True)
    handle = models.CharField(max_length = 255)
    image = JSONField(null = True, dump_kwargs = {'cls': ShopifyDjangoJSONEncoder})
    published = models.BooleanField(default = True)
    published_at = models.DateTimeField(null = True)
    published_scope = models.CharField(max_length = 16, default = 'global')
    sort_order = models.CharField(max_length = 16)
    template_suffix = models.CharField(max_length = 32, null = True)
    title = models.CharField(max_length = 255)
    updated_at = models.DateTimeField()

    @property
    def collects(self):
        return Collect.objects.filter(self.user, collection_id = self.id)
