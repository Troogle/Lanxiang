# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Beatmap.mapname'
        db.add_column('ctb_beatmap', 'mapname',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Beatmap.mode'
        db.add_column('ctb_beatmap', 'mode',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=10),
                      keep_default=False)

        # Adding field 'Beatmap.date'
        db.add_column('ctb_beatmap', 'date',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Play.order'
        db.add_column('ctb_play', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Beatmap.mapname'
        db.delete_column('ctb_beatmap', 'mapname')

        # Deleting field 'Beatmap.mode'
        db.delete_column('ctb_beatmap', 'mode')

        # Deleting field 'Beatmap.date'
        db.delete_column('ctb_beatmap', 'date')

        # Deleting field 'Play.order'
        db.delete_column('ctb_play', 'order')


    models = {
        'ctb.beatmap': {
            'Meta': {'object_name': 'Beatmap'},
            'date': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'diffid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'maxscore': ('django.db.models.fields.IntegerField', [], {}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '10'})
        },
        'ctb.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpid': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.IntegerField', [], {})
        },
        'ctb.matchuser': {
            'Meta': {'object_name': 'MatchUser'},
            'checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'osuid': ('django.db.models.fields.IntegerField', [], {}),
            'point': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7', 'default': '0'}),
            'userType': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'ctb.play': {
            'Meta': {'object_name': 'Play'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ctb.Beatmap']"}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ctb.Match']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ctb.MatchUser']"}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ctb']