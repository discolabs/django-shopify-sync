from .base import ShopifyResourceModel
from django.db import models
import shopify


class CarrierService(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.CarrierService

    CARRIER_SERVICE_TYPE_API = 'api'
    CARRIER_SERVICE_TYPE_LEGACY = 'legacy'
    CARRIER_SERVICE_TYPES = (
        (CARRIER_SERVICE_TYPE_API, 'API'),
        (CARRIER_SERVICE_TYPE_LEGACY, 'Legacy'),
    )

    FORMAT_JSON = 'json'
    FORMAT_XML = 'xml'
    FORMATS = (
        (FORMAT_JSON, 'JSON'),
        (FORMAT_XML, 'XML'),
    )

    active = models.BooleanField(default = True)
    callback_url = models.URLField()
    carrier_service_type = models.CharField(max_length = 16, choices = CARRIER_SERVICE_TYPES, default = CARRIER_SERVICE_TYPE_API)
    format = models.CharField(max_length = 8, choices = FORMATS, default = FORMAT_JSON)
    name = models.CharField(max_length = 255)
    service_discovery = models.BooleanField(default = True)

    class Meta:
        app_label = 'shopify_sync'
