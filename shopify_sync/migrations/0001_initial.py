# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Collect'
        db.create_table(u'shopify_sync_collect', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_options_app.ProductOptionsAppUser'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('collection_id', self.gf('django.db.models.fields.IntegerField')()),
            ('featured', self.gf('django.db.models.fields.BooleanField')()),
            ('position', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('product_id', self.gf('django.db.models.fields.IntegerField')()),
            ('sort_value', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
        ))
        db.send_create_signal('shopify_sync', ['Collect'])

        # Adding model 'CustomCollection'
        db.create_table(u'shopify_sync_customcollection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_options_app.ProductOptionsAppUser'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('body_html', self.gf('django.db.models.fields.TextField')(null=True)),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('jsonfield.fields.JSONField')(null=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('published_scope', self.gf('django.db.models.fields.CharField')(default='global', max_length=16)),
            ('sort_order', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('template_suffix', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('shopify_sync', ['CustomCollection'])

        # Adding model 'Product'
        db.create_table(u'shopify_sync_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_options_app.ProductOptionsAppUser'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('body_html', self.gf('django.db.models.fields.TextField')()),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('product_type', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('published_scope', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('template_suffix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('shopify_sync', ['Product'])

        # Adding model 'ScriptTag'
        db.create_table(u'shopify_sync_scripttag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_options_app.ProductOptionsAppUser'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('src', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('shopify_sync', ['ScriptTag'])

        # Adding model 'Shop'
        db.create_table(u'shopify_sync_shop', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_options_app.ProductOptionsAppUser'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('myshopify_domain', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('shop_owner', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('customer_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('province_code', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('country_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=4)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=4)),
            ('timezone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=4, null=True)),
            ('money_format', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('money_in_emails_format', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('money_with_currency_format', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('money_with_currency_in_emails_format', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('county_taxes', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('tax_shipping', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('taxes_included', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('google_apps_domain', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('google_apps_login_enabled', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('plan_name', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('plan_display_name', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('password_enabled', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
            ('primary_location_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('public', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
            ('eligible_for_payments', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
            ('requires_extra_payments_agreement', self.gf('django.db.models.fields.NullBooleanField')(default=True, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
        ))
        db.send_create_signal('shopify_sync', ['Shop'])

        # Adding model 'SmartCollection'
        db.create_table(u'shopify_sync_smartcollection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_options_app.ProductOptionsAppUser'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('body_html', self.gf('django.db.models.fields.TextField')(null=True)),
            ('handle', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('jsonfield.fields.JSONField')(null=True)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('published_scope', self.gf('django.db.models.fields.CharField')(default='global', max_length=16)),
            ('rules', self.gf('jsonfield.fields.JSONField')()),
            ('disjunctive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sort_order', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('template_suffix', self.gf('django.db.models.fields.CharField')(max_length=32, null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('shopify_sync', ['SmartCollection'])

        # Adding model 'Webhook'
        db.create_table(u'shopify_sync_webhook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product_options_app.ProductOptionsAppUser'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('address', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('fields', self.gf('jsonfield.fields.JSONField')(null=True)),
            ('metafield_namespaces', self.gf('jsonfield.fields.JSONField')(null=True)),
        ))
        db.send_create_signal('shopify_sync', ['Webhook'])


    def backwards(self, orm):
        # Deleting model 'Collect'
        db.delete_table(u'shopify_sync_collect')

        # Deleting model 'CustomCollection'
        db.delete_table(u'shopify_sync_customcollection')

        # Deleting model 'Product'
        db.delete_table(u'shopify_sync_product')

        # Deleting model 'ScriptTag'
        db.delete_table(u'shopify_sync_scripttag')

        # Deleting model 'Shop'
        db.delete_table(u'shopify_sync_shop')

        # Deleting model 'SmartCollection'
        db.delete_table(u'shopify_sync_smartcollection')

        # Deleting model 'Webhook'
        db.delete_table(u'shopify_sync_webhook')


    models = {
        'product_options_app.productoptionsappuser': {
            'Meta': {'object_name': 'ProductOptionsAppUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'myshopify_domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'uninstalled'", 'max_length': '16'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'shopify_sync.collect': {
            'Meta': {'object_name': 'Collect'},
            'collection_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'product_id': ('django.db.models.fields.IntegerField', [], {}),
            'sort_value': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product_options_app.ProductOptionsAppUser']"})
        },
        'shopify_sync.customcollection': {
            'Meta': {'object_name': 'CustomCollection'},
            'body_html': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('jsonfield.fields.JSONField', [], {'null': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'published_scope': ('django.db.models.fields.CharField', [], {'default': "'global'", 'max_length': '16'}),
            'sort_order': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'template_suffix': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product_options_app.ProductOptionsAppUser']"})
        },
        'shopify_sync.product': {
            'Meta': {'object_name': 'Product'},
            'body_html': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'published_scope': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product_options_app.ProductOptionsAppUser']"}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'shopify_sync.scripttag': {
            'Meta': {'object_name': 'ScriptTag'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'src': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product_options_app.ProductOptionsAppUser']"})
        },
        'shopify_sync.shop': {
            'Meta': {'object_name': 'Shop'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'county_taxes': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True'}),
            'customer_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'eligible_for_payments': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            'google_apps_domain': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'google_apps_login_enabled': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '4'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '4'}),
            'money_format': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'money_in_emails_format': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'money_with_currency_format': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'money_with_currency_in_emails_format': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'myshopify_domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'password_enabled': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'plan_display_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'plan_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'primary_location_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'province_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'public': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'requires_extra_payments_agreement': ('django.db.models.fields.NullBooleanField', [], {'default': 'True', 'null': 'True', 'blank': 'True'}),
            'shop_owner': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'tax_shipping': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'taxes_included': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product_options_app.ProductOptionsAppUser']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'})
        },
        'shopify_sync.smartcollection': {
            'Meta': {'object_name': 'SmartCollection'},
            'body_html': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'disjunctive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('jsonfield.fields.JSONField', [], {'null': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'published_scope': ('django.db.models.fields.CharField', [], {'default': "'global'", 'max_length': '16'}),
            'rules': ('jsonfield.fields.JSONField', [], {}),
            'sort_order': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'template_suffix': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product_options_app.ProductOptionsAppUser']"})
        },
        'shopify_sync.webhook': {
            'Meta': {'object_name': 'Webhook'},
            'address': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fields': ('jsonfield.fields.JSONField', [], {'null': 'True'}),
            'format': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'metafield_namespaces': ('jsonfield.fields.JSONField', [], {'null': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product_options_app.ProductOptionsAppUser']"})
        }
    }

    complete_apps = ['shopify_sync']