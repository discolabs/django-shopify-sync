from .base import ShopifyResourceModel
from django.db import models
import shopify


class Shop(ShopifyResourceModel):
    shopify_resource = shopify.resources.Shop
    created_at = models.DateTimeField()

    myshopify_domain = models.CharField(max_length = 255, unique = True)
    domain = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    shop_owner = models.CharField(max_length = 255)
    email = models.EmailField()
    customer_email = models.EmailField()
    phone = models.CharField(max_length = 32)

    address1 = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    zip = models.CharField(max_length = 16)
    province = models.CharField(max_length = 255)
    province_code = models.CharField(max_length = 32)
    country = models.CharField(max_length = 255)
    country_code = models.CharField(max_length = 32)
    country_name = models.CharField(max_length = 255)
    latitude = models.DecimalField(max_digits = 7, decimal_places = 4)
    longitude = models.DecimalField(max_digits = 7, decimal_places = 4)
    timezone = models.CharField(max_length = 255)

    currency = models.CharField(max_length = 4)
    money_format = models.CharField(max_length = 32)
    money_in_emails_format = models.CharField(max_length = 32)
    money_with_currency_format = models.CharField(max_length = 32)
    money_with_currency_in_emails_format = models.CharField(max_length = 32)

    county_taxes = models.BooleanField()
    tax_shipping = models.BooleanField()
    taxes_included = models.BooleanField()

    google_apps_domain = models.CharField(max_length = 255)
    google_apps_login_enabled = models.BooleanField()

    plan_name = models.CharField(max_length = 32)
    plan_display_name = models.CharField(max_length = 32)
    password_enabled = models.BooleanField()

    # Undocumented properties
    primary_location_id = models.IntegerField()
    public = models.BooleanField()
    eligible_for_payments = models.BooleanField()
    requires_extra_payments_agreement = models.BooleanField()
    source = models.CharField(max_length = 32)

    class Meta:
        abstract = True