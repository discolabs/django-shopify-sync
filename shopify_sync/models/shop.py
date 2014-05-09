from .base import ShopifyResourceModel
from django.db import models
import shopify


class Shop(ShopifyResourceModel):
    shopify_resource_class = shopify.resources.Shop
    created_at = models.DateTimeField()

    myshopify_domain = models.CharField(max_length = 255, unique = True)
    domain = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255, null = True)
    shop_owner = models.CharField(max_length = 255, null = True)
    email = models.EmailField(null = True)
    customer_email = models.EmailField(null = True)
    phone = models.CharField(max_length = 32, null = True)

    address1 = models.CharField(max_length = 255, null = True)
    city = models.CharField(max_length = 255, null = True)
    zip = models.CharField(max_length = 16, null = True)
    province = models.CharField(max_length = 255, null = True)
    province_code = models.CharField(max_length = 32, null = True)
    country = models.CharField(max_length = 255, null = True)
    country_code = models.CharField(max_length = 32, null = True)
    country_name = models.CharField(max_length = 255, null = True)
    latitude = models.DecimalField(max_digits = 7, decimal_places = 4, null = True)
    longitude = models.DecimalField(max_digits = 7, decimal_places = 4, null = True)
    timezone = models.CharField(max_length = 255, null = True)

    currency = models.CharField(max_length = 4, null = True)
    money_format = models.CharField(max_length = 32, null = True)
    money_in_emails_format = models.CharField(max_length = 32, null = True)
    money_with_currency_format = models.CharField(max_length = 32, null = True)
    money_with_currency_in_emails_format = models.CharField(max_length = 32, null = True)

    county_taxes = models.NullBooleanField(default = False, null = True)
    tax_shipping = models.NullBooleanField(default = False, null = True)
    taxes_included = models.NullBooleanField(default = False, null = True)

    google_apps_domain = models.CharField(max_length = 255, null = True)
    google_apps_login_enabled = models.NullBooleanField(default = False, null = True)

    plan_name = models.CharField(max_length = 32, null = True)
    plan_display_name = models.CharField(max_length = 32, null = True)
    password_enabled = models.NullBooleanField(default = False, null = True)

    # Undocumented properties
    primary_location_id = models.IntegerField(null = True)
    public = models.NullBooleanField(default = True, null = True)
    eligible_for_payments = models.NullBooleanField(default = True, null = True)
    requires_extra_payments_agreement = models.NullBooleanField(default = True, null = True)
    source = models.CharField(max_length = 32, null = True)

    @classmethod
    def sync_for_user(cls, user, **kwargs):
        with user.session:
            shopify_shop = cls.shopify_resource_class.current()
        cls(user = user, shopify_resource = shopify_shop).save()

    class Meta:
        abstract = True