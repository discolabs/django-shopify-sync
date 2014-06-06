from django.db import models

from owned_models.models import UserOwnedModel, UserOwnedModelManager

import shopify


class SmartCollectManager(UserOwnedModelManager):

    def sync_for_user(self, user, smart_collection, shopify_product):
        local_model, created = self.get_or_create(user = user, collection_id = smart_collection.id, product_id = shopify_product.id)
        return local_model


    def sync_all_for_user(self, user, smart_collections, **kwargs):
        local_models = []
        for smart_collection in smart_collections:
            with user.session:
                shopify_products = shopify.Product.find(collection_id = smart_collection.id)
            for shopify_product in shopify_products:
                local_models.append(self.sync_for_user(user, smart_collection, shopify_product))
        return local_models


class SmartCollect(UserOwnedModel):

    collection_id = models.IntegerField()
    product_id = models.IntegerField()

    objects = SmartCollectManager()

    class Meta:
        app_label = 'shopify_sync'