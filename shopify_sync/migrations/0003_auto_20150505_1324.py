# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import shopify_sync.encoders


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_sync', '0002_auto_20150505_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineitem',
            name='product_exists',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lineitem',
            name='properties',
            field=jsonfield.fields.JSONField(default=shopify_sync.encoders.empty_list),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lineitem',
            name='total_discount',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lineitem',
            name='tax_lines',
            field=jsonfield.fields.JSONField(default=shopify_sync.encoders.empty_list),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='discount_codes',
            field=jsonfield.fields.JSONField(default=shopify_sync.encoders.empty_list),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_lines',
            field=jsonfield.fields.JSONField(default=shopify_sync.encoders.empty_list),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='tax_lines',
            field=jsonfield.fields.JSONField(default=shopify_sync.encoders.empty_list),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='smartcollection',
            name='rules',
            field=jsonfield.fields.JSONField(default=shopify_sync.encoders.empty_list),
            preserve_default=True,
        ),
    ]
