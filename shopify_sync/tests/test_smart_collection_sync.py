from ..models import SmartCollection
from shopify.resources import SmartCollection as ShopifySmartCollection

from shopify_webhook.tests import AbstractWebhookTestCase

from .recipes import UserRecipe
from datetime import datetime


class SmartCollectionSyncTestCase(AbstractWebhookTestCase):

    def test_smart_collection_created_on_direct_sync(self):
        # Get a user to test with.
        user = UserRecipe.make(id = 1)

        # Get a 'remote' resource.
        shopify_resource = ShopifySmartCollection()
        shopify_resource.id = 123
        shopify_resource.rules = []
        shopify_resource.created_at = datetime.now()
        shopify_resource.updated_at = datetime.now()

        # Perform synchronisation from the Shopify resource.
        for i in range(1, 3):
            # Set the title based on the iteration number.
            shopify_resource.title = "SmartCollection #{0}".format(i)

            # Perform the syncronisation.
            SmartCollection.objects.sync_one(user, shopify_resource)

            # Fetch the smart collections for the user and verify synchronisation worked correctly.
            smart_collections = SmartCollection.objects.all(user)
            self.assertEqual(len(smart_collections), 1, "Smart Collection was synced to database.")

            # Check we can fetch that collection from the database by ID and that its attributes are correct.
            smart_collection = SmartCollection.objects.get(user, id = 123)
            self.assertEqual(shopify_resource.id, smart_collection.id, "Smart Collection ID attribute was synced to the database.")
            self.assertEqual(shopify_resource.title, smart_collection.title, "Smart Collection title attribute was synced to the database.")

    def test_smart_collection_created_on_webhook(self):
        # Create a test domain.
        domain = 'test.myshopify.com'

        # Get a user to test with.
        user = UserRecipe.make(id = 1, username = domain)

        # Get the data to send in the POST.
        data = self.read_fixture('smartcollection_created')

        # Make a webhook request.
        response = self.post_shopify_webhook(topic = 'collections/create', domain = domain, data = data)
        self.assertEqual(response.status_code, 200, 'POST collections/create request with valid HMAC returns 200 (OK).')

        # Fetch the smart collections for the user and verify synchronisation worked correctly.
        smart_collections = SmartCollection.objects.all(user)
        self.assertEqual(len(smart_collections), 1, "Smart Collection was synced to database.")

        # Check we can fetch that collection from the database by ID and that its attributes are correct.
        smart_collection = SmartCollection.objects.get(user, id = data['id'])
        self.assertEqual(data['id'], smart_collection.id, "Smart Collection ID attribute was synced to the database.")
        self.assertEqual(data['title'], smart_collection.title, "Smart Collection title attribute was synced to the database.")
