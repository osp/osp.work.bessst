# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'People'
        db.create_table('people_people', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prefix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('people', ['People'])


    def backwards(self, orm):
        # Deleting model 'People'
        db.delete_table('people_people')


    models = {
        'people.people': {
            'Meta': {'object_name': 'People'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['people']