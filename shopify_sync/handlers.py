from .models import SmartCollection
from .models import CustomCollection
from .models import Product
from .models import Shop

from django.contrib.auth import get_user_model


def get_topic_model(topic, data):
    """
    Return the model related to the given topic, if it's a valid topic permitted by theme settings.
    If the topic isn't permitted, or there's no rule mapping the given topic to a model, None is returned.
    """
    if topic.startswith('collections/'):
        if 'rules' in data:
            return SmartCollection
        return CustomCollection

    if topic.startswith('products/'):
        return Product

    if topic.startswith('shop/'):
        return Shop

    return None


def get_topic_action(topic):
    return 'sync_one'


def webhook_received_handler(sender, domain, topic, data, **kwargs):
    """
    Signal handler to process a received webhook.
    """
        
    # Check that we know which user is related to this incoming webhook.
    # Assumes the USERNAME_FIELD on the user model is equivalent to the domain.
    user_model = get_user_model()
    try:
        user = user_model.objects.get(**{
            user_model.USERNAME_FIELD: domain 
        })
    except user_model.DoesNotExist:
        return

    # Get the model related to the incoming topic and data.
    model = get_topic_model(topic, data)
    if model is None:
        return

    # Get the action related to the incoming topic.
    model_action = get_topic_action(topic)
    if model_action is None:
        return

    # Convert the incoming data to the relevant Shopify resource.
    shopify_resource = model.shopify_resource_from_json(data)

    # Execute the desired action.
    if model_action == 'sync_one':
        model.objects.sync_one(user, shopify_resource)
