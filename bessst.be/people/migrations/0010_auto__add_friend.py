# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Friend'
        db.create_table('people_friend', (
            ('individual_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['people.Individual'], unique=True, primary_key=True)),
            ('location_coordinates', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location_explanation', self.gf('django.db.models.fields.TextField')()),
            ('newsletter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('people', ['Friend'])


    def backwards(self, orm):
        # Deleting model 'Friend'
        db.delete_table('people_friend')


    models = {
        'people.friend': {
            'Meta': {'object_name': 'Friend', '_ormbases': ['people.Individual']},
            'display': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'individual_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.Individual']", 'unique': 'True', 'primary_key': 'True'}),
            'location_coordinates': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location_explanation': ('django.db.models.fields.TextField', [], {}),
            'newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'people.individual': {
            'Meta': {'object_name': 'Individual', '_ormbases': ['people.People']},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'people_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.People']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.organization': {
            'Meta': {'object_name': 'Organization', '_ormbases': ['people.People']},
            'contact_person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contact_person'", 'null': 'True', 'to': "orm['people.Individual']"}),
            'individuals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'individual_set'", 'blank': 'True', 'to': "orm['people.Individual']"}),
            'people_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.People']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.people': {
            'Meta': {'object_name': 'People'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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