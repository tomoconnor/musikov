# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MidiChain'
        db.create_table('musikovweb_midichain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fileName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('filePath', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rank', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('transitionMatrix', self.gf('django.db.models.fields.TextField')()),
            ('noteMapping', self.gf('django.db.models.fields.TextField')()),
            ('inverseNoteMapping', self.gf('django.db.models.fields.TextField')()),
            ('transitionFrequencies', self.gf('django.db.models.fields.TextField')()),
            ('transitionSum', self.gf('django.db.models.fields.FloatField')()),
            ('pngFile', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('svgFile', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dotFile', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('musikovweb', ['MidiChain'])


    def backwards(self, orm):
        # Deleting model 'MidiChain'
        db.delete_table('musikovweb_midichain')


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
        }
    }

    complete_apps = ['musikovweb']