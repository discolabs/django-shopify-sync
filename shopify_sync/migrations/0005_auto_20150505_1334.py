# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_sync', '0004_remove_carrierservice_format'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='lineitem',
            name='variant',
        ),
        migrations.AddField(
            model_name='lineitem',
            name='product_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lineitem',
            name='variant_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
