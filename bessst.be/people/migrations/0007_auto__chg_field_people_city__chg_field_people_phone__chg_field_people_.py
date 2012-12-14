# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'People.city'
        db.alter_column('people_people', 'city', self.gf('django.db.models.fields.CharField')(max_length=80, null=True))

        # Changing field 'People.phone'
        db.alter_column('people_people', 'phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'People.link'
        db.alter_column('people_people', 'link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'People.address'
        db.alter_column('people_people', 'address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'People.email'
        db.alter_column('people_people', 'email', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'People.city'
        db.alter_column('people_people', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=80))

        # Changing field 'People.phone'
        db.alter_column('people_people', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=20))

        # Changing field 'People.link'
        db.alter_column('people_people', 'link', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

        # Changing field 'People.address'
        db.alter_column('people_people', 'address', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'People.email'
        db.alter_column('people_people', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=100))

    models = {
        'people.individual': {
            'Meta': {'object_name': 'Individual', '_ormbases': ['people.People']},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'people_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.People']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.organization': {
            'Meta': {'object_name': 'Organization', '_ormbases': ['people.People']},
            'contact_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact_person'", 'to': "orm['people.Individual']"}),
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