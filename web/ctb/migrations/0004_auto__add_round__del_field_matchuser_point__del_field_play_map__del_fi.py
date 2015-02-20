# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Round'
        db.create_table(u'ctb_round', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ctb.Match'])),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ctb.Beatmap'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'ctb', ['Round'])

        # Deleting field 'MatchUser.point'
        db.delete_column(u'ctb_matchuser', 'point')

        # Deleting field 'Play.map'
        db.delete_column(u'ctb_play', 'map_id')

        # Deleting field 'Play.order'
        db.delete_column(u'ctb_play', 'order')

        # Deleting field 'Play.match'
        db.delete_column(u'ctb_play', 'match_id')

        # Adding field 'Play.round'
        db.add_column(u'ctb_play', 'round',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ctb.Round'], null=True),
                      keep_default=False)

        # Adding field 'Play.failed'
        db.add_column(u'ctb_play', 'failed',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Round'
        db.delete_table(u'ctb_round')

        # Adding field 'MatchUser.point'
        db.add_column(u'ctb_matchuser', 'point',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=7),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Play.map'
        raise RuntimeError("Cannot reverse this migration. 'Play.map' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Play.map'
        db.add_column(u'ctb_play', 'map',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ctb.Beatmap']),
                      keep_default=False)

        # Adding field 'Play.order'
        db.add_column(u'ctb_play', 'order',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Play.match'
        raise RuntimeError("Cannot reverse this migration. 'Play.match' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Play.match'
        db.add_column(u'ctb_play', 'match',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ctb.Match']),
                      keep_default=False)

        # Deleting field 'Play.round'
        db.delete_column(u'ctb_play', 'round_id')

        # Deleting field 'Play.failed'
        db.delete_column(u'ctb_play', 'failed')


    models = {
        u'ctb.beatmap': {
            'Meta': {'object_name': 'Beatmap'},
            'date': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'diffid': ('django.db.models.fields.IntegerField', [], {}),
            'diffname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'maxscore': ('django.db.models.fields.IntegerField', [], {}),
            'mode': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '10'})
        },
        u'ctb.match': {
            'Meta': {'object_name': 'Match'},
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
            'score': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ctb.round': {
            'Meta': {'object_name': 'Round'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ctb.Beatmap']"}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ctb.Match']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['ctb']