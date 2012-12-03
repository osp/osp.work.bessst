# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=80, null=True)),
            ('axis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['axis.Axis'])),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding M2M table for field authors on 'Project'
        db.create_table('projects_project_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('people', models.ForeignKey(orm['people.people'], null=False))
        ))
        db.create_unique('projects_project_authors', ['project_id', 'people_id'])

        # Adding M2M table for field producers on 'Project'
        db.create_table('projects_project_producers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['projects.project'], null=False)),
            ('people', models.ForeignKey(orm['people.people'], null=False))
        ))
        db.create_unique('projects_project_producers', ['project_id', 'people_id'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Removing M2M table for field authors on 'Project'
        db.delete_table('projects_project_authors')

        # Removing M2M table for field producers on 'Project'
        db.delete_table('projects_project_producers')


    models = {
        'axis.axis': {
            'Meta': {'object_name': 'Axis'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'author_set'", 'symmetrical': 'False', 'to': "orm['people.People']"}),
            'axis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['axis.Axis']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True'}),
            'producers': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'producer_set'", 'symmetrical': 'False', 'to': "orm['people.People']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['projects']