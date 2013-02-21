# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'People.biography_en'
        db.add_column('people_people', 'biography_en',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'People.biography_fr'
        db.add_column('people_people', 'biography_fr',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'People.biography_en'
        db.delete_column('people_people', 'biography_en')

        # Deleting field 'People.biography_fr'
        db.delete_column('people_people', 'biography_fr')


    models = {
        'people.friend': {
            'Meta': {'ordering': "['name']", 'object_name': 'Friend', '_ormbases': ['people.Individual']},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'individual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.Individual']", 'unique': 'True', 'primary_key': 'True'}),
            'location_explanation': ('django.db.models.fields.TextField', [], {}),
            'location_latitude': ('django.db.models.fields.FloatField', [], {}),
            'location_longitude': ('django.db.models.fields.FloatField', [], {}),
            'newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'people.individual': {
            'Meta': {'ordering': "['name']", 'object_name': 'Individual', '_ormbases': ['people.People']},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'people_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.People']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.organization': {
            'Meta': {'ordering': "['name']", 'object_name': 'Organization', '_ormbases': ['people.People']},
            'contact_person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_person'", 'null': 'True', 'to': "orm['people.Individual']"}),
            'individuals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'individual_set'", 'blank': 'True', 'to': "orm['people.Individual']"}),
            'people_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.People']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.people': {
            'Meta': {'ordering': "['name']", 'object_name': 'People'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'biography_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'biography_fr': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['people']