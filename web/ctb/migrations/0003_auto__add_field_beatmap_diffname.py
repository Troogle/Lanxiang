# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Beatmap.diffname'
        db.add_column('ctb_beatmap', 'diffname',
                      self.gf('django.db.models.fields.CharField')(max_length=255, default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Beatmap.diffname'
        db.delete_column('ctb_beatmap', 'diffname')


    models = {
        'ctb.beatmap': {
            'Meta': {'object_name': 'Beatmap'},
            'date': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'diffid': ('django.db.models.fields.IntegerField', [], {}),
            'diffname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'maxscore': ('django.db.models.fields.IntegerField', [], {}),
            'mode': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'None'"})
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
            'point': ('django.db.models.fields.DecimalField', [], {'decimal_places': '7', 'max_digits': '10', 'default': '0'}),
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