# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FlatPage.title_en'
        db.add_column('flatpages_flatpage', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=255),
                      keep_default=False)

        # Adding field 'FlatPage.title_fr'
        db.add_column('flatpages_flatpage', 'title_fr',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=255),
                      keep_default=False)

        # Adding field 'FlatPage.content_en'
        db.add_column('flatpages_flatpage', 'content_en',
                      self.gf('django.db.models.fields.TextField')(default=' '),
                      keep_default=False)

        # Adding field 'FlatPage.content_fr'
        db.add_column('flatpages_flatpage', 'content_fr',
                      self.gf('django.db.models.fields.TextField')(default=' '),
                      keep_default=False)

        # Adding field 'FlatPage.infobox_en'
        db.add_column('flatpages_flatpage', 'infobox_en',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'FlatPage.infobox_fr'
        db.add_column('flatpages_flatpage', 'infobox_fr',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FlatPage.title_en'
        db.delete_column('flatpages_flatpage', 'title_en')

        # Deleting field 'FlatPage.title_fr'
        db.delete_column('flatpages_flatpage', 'title_fr')

        # Deleting field 'FlatPage.content_en'
        db.delete_column('flatpages_flatpage', 'content_en')

        # Deleting field 'FlatPage.content_fr'
        db.delete_column('flatpages_flatpage', 'content_fr')

        # Deleting field 'FlatPage.infobox_en'
        db.delete_column('flatpages_flatpage', 'infobox_en')

        # Deleting field 'FlatPage.infobox_fr'
        db.delete_column('flatpages_flatpage', 'infobox_fr')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'flatpages.flatpage': {
            'Meta': {'object_name': 'FlatPage'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_en': ('django.db.models.fields.TextField', [], {}),
            'content_fr': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infobox': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'infobox_en': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'infobox_fr': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'media_app.document': {
            'Meta': {'object_name': 'Document'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'media_app.image': {
            'Meta': {'object_name': 'Image'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['flatpages']