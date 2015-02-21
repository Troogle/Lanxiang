# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Play.useful'
        db.add_column(u'ctb_play', 'useful',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Play.useful'
        db.delete_column(u'ctb_play', 'useful')


    models = {
        u'ctb.beatmap': {
            'Meta': {'object_name': 'Beatmap'},
            'date': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'diffid': ('django.db.models.fields.IntegerField', [], {}),
            'diffname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'maxscore': ('django.db.models.fields.IntegerField', [], {}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '10'}),
            'setid': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'ctb.match': {
            'Meta': {'ordering': "['-date', '-time']", 'object_name': 'Match'},
            'date': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpid': ('django.db.models.fields.IntegerField', [], {}),
            'time': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ctb.matchuser': {
            'Meta': {'object_name': 'MatchUser'},
            'checked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'osuid': ('django.db.models.fields.IntegerField', [], {}),
            'userType': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'ctb.play': {
            'Meta': {'object_name': 'Play'},
            'failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ctb.MatchUser']"}),
            'round': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ctb.Round']", 'null': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'useful': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ctb.round': {
            'Meta': {'ordering': "['order']", 'object_name': 'Round'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ctb.Beatmap']"}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ctb.Match']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ctb']