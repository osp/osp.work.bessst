# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Axis.pictogram'
        db.alter_column('axis_axis', 'pictogram', self.gf('django.db.models.fields.CharField')(max_length='20'))

    def backwards(self, orm):

        # Changing field 'Axis.pictogram'
        db.alter_column('axis_axis', 'pictogram', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        'axis.axis': {
            'Meta': {'object_name': 'Axis'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'pictogram': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        }
    }

    complete_apps = ['axis']