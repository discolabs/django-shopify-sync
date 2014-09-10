from django.apps import AppConfig
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from shopify_webhook.signals import webhook_received
from shopify_sync.handlers import webhook_received_handler

import shopify


class ShopifySyncConfig(AppConfig):
    """
    Application configuration for the Shopify Sync application.
    """

    name = 'shopify_sync'
    verbose_name = 'Shopify Sync'

    def ready(self):
        """
        The ready() method is called after Django setup.
        """

        # Connect shopify_webhook's webhook_received signal to our synchronisation handler.
        webhook_received.connect(webhook_received_handler, dispatch_uid = 'shopify_sync_webhook_received_handler')
