# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadedFile'
        db.create_table('musikovweb_uploadedfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uploadfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('musikovweb', ['UploadedFile'])


    def backwards(self, orm):
        # Deleting model 'UploadedFile'
        db.delete_table('musikovweb_uploadedfile')


    models = {
        'musikovweb.midichain': {
            'Meta': {'object_name': 'MidiChain'},
            'dotFile': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fileName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'filePath': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inverseNoteMapping': ('django.db.models.fields.TextField', [], {}),
            'noteMapping': ('django.db.models.fields.TextField', [], {}),
            'pngFile': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rank': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'svgFile': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'transitionFrequencies': ('django.db.models.fields.TextField', [], {}),
            'transitionMatrix': ('django.db.models.fields.TextField', [], {}),
            'transitionSum': ('django.db.models.fields.FloatField', [], {})
        },
        'musikovweb.uploadedfile': {
            'Meta': {'object_name': 'UploadedFile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uploadfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['musikovweb']