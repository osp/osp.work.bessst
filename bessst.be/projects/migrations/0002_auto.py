# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field authors on 'Project'
        db.delete_table('projects_project_authors')

        # Adding M2M table for field partners on 'Project'
        db.create_table('projects_project_partners', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('people', models.ForeignKey(orm['people.people'], null=False))
        ))
        db.create_unique('projects_project_partners', ['project_id', 'people_id'])


    def backwards(self, orm):
        # Adding M2M table for field authors on 'Project'
        db.create_table('projects_project_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('people', models.ForeignKey(orm['people.people'], null=False))
        ))
        db.create_unique('projects_project_authors', ['project_id', 'people_id'])

        # Removing M2M table for field partners on 'Project'
        db.delete_table('projects_project_partners')


    models = {
        'axis.axis': {
            'Meta': {'object_name': 'Axis'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pictogram': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'media_app.image': {
            'Meta': {'object_name': 'Image'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'people.people': {
            'Meta': {'object_name': 'People'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'axis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['axis.Axis']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'partner_set'", 'symmetrical': 'False', 'to': "orm['people.People']"}),
            'producers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'producer_set'", 'symmetrical': 'False', 'to': "orm['people.People']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['projects']