# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Resource.axis'
        db.delete_column('resources_resource', 'axis_id')

        # Adding field 'Resource.category'
        db.add_column('resources_resource', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['resources.ResourceCategory']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Resource.axis'
        db.add_column('resources_resource', 'axis',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['resources.ResourceCategory']),
                      keep_default=False)

        # Deleting field 'Resource.category'
        db.delete_column('resources_resource', 'category_id')


    models = {
        'resources.resource': {
            'Meta': {'object_name': 'Resource'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['resources.ResourceCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'resources.resourcecategory': {
            'Meta': {'object_name': 'ResourceCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['resources']