# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify_sync', '0003_auto_20150505_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrierservice',
            name='format',
        ),
    ]
