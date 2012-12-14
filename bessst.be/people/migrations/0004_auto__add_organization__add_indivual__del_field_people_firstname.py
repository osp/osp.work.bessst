# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Organization'
        db.create_table('people_organization', (
            ('people_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['people.People'], unique=True, primary_key=True)),
            ('contact_person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contact_person', to=orm['people.People'])),
        ))
        db.send_create_signal('people', ['Organization'])

        # Adding model 'Indivual'
        db.create_table('people_indivual', (
            ('people_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['people.People'], unique=True, primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('people', ['Indivual'])

        # Deleting field 'People.firstname'
        db.delete_column('people_people', 'firstname')


    def backwards(self, orm):
        # Deleting model 'Organization'
        db.delete_table('people_organization')

        # Deleting model 'Indivual'
        db.delete_table('people_indivual')

        # Adding field 'People.firstname'
        db.add_column('people_people', 'firstname',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    models = {
        'people.indivual': {
            'Meta': {'object_name': 'Indivual', '_ormbases': ['people.People']},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'people_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.People']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.organization': {
            'Meta': {'object_name': 'Organization', '_ormbases': ['people.People']},
            'contact_person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contact_person'", 'to': "orm['people.People']"}),
            'people_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['people.People']", 'unique': 'True', 'primary_key': 'True'})
        },
        'people.people': {
            'Meta': {'object_name': 'People'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['people']