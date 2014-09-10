from django.test import TestCase

from shopify_sync.models import SmartCollection
from shopify.resources import SmartCollection as ShopifySmartCollection

from .recipes import UserRecipe, SmartCollectionRecipe
from datetime import datetime


class SmartCollectionSyncTestCase(TestCase):

    def test_smart_collection_created_on_sync(self):
        # Get a user to test with.
        user = UserRecipe.make(id = 1)

        # Get a 'remote' resource.
        shopify_resource = ShopifySmartCollection()
        shopify_resource.id = 123
        shopify_resource.rules = []
        shopify_resource.created_at = datetime.now()
        shopify_resource.updated_at = datetime.now()

        # Perform synchronisation from the Shopify resource.
        SmartCollection.objects.sync_one(user, shopify_resource)

        # Fetch the smart collections for the user and verify synchronisation worked correctly.
        smart_collection = SmartCollection.objects.get(user, id = 123)

        self.assertEqual(shopify_resource.id, smart_collection.id, "Synced OK")
