# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FlatPage.content'
        db.alter_column('flatpages_flatpage', 'content', self.gf('wymeditor.models.WYMEditorField')())

        # Changing field 'FlatPage.infobox'
        db.alter_column('flatpages_flatpage', 'infobox', self.gf('wymeditor.models.WYMEditorField')())

    def backwards(self, orm):

        # Changing field 'FlatPage.content'
        db.alter_column('flatpages_flatpage', 'content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'FlatPage.infobox'
        db.alter_column('flatpages_flatpage', 'infobox', self.gf('django.db.models.fields.TextField')())

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
            'content': ('wymeditor.models.WYMEditorField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infobox': ('wymeditor.models.WYMEditorField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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