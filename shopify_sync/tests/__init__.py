from shopify_webhook.tests import WebhookTestCase


class SyncTestCase(WebhookTestCase):
    """
    Base class providing helpers for running synchronisation-based tests.
    """

    def assertSynced(self, user, data, model):
        """
        Check that the given data has been synchronised locally for the given user and model class.
        """
        instance = model.objects.get(user, id = data['id'])
