# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MatchUser'
        db.create_table('ctb_matchuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('osuid', self.gf('django.db.models.fields.IntegerField')()),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('checked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('point', self.gf('django.db.models.fields.DecimalField')(decimal_places=7, max_digits=10, default=0)),
            ('userType', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ctb', ['MatchUser'])

        # Adding model 'Beatmap'
        db.create_table('ctb_beatmap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diffid', self.gf('django.db.models.fields.IntegerField')()),
            ('maxscore', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ctb', ['Beatmap'])

        # Adding model 'Match'
        db.create_table('ctb_match', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mpid', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.IntegerField')()),
            ('time', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ctb', ['Match'])

        # Adding model 'Play'
        db.create_table('ctb_play', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ctb.MatchUser'])),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ctb.Match'])),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ctb.Beatmap'])),
        ))
        db.send_create_signal('ctb', ['Play'])


    def backwards(self, orm):
        # Deleting model 'MatchUser'
        db.delete_table('ctb_matchuser')

        # Deleting model 'Beatmap'
        db.delete_table('ctb_beatmap')

        # Deleting model 'Match'
        db.delete_table('ctb_match')

        # Deleting model 'Play'
        db.delete_table('ctb_play')


    models = {
        'ctb.beatmap': {
            'Meta': {'object_name': 'Beatmap'},
            'diffid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maxscore': ('django.db.models.fields.IntegerField', [], {})
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
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ctb.MatchUser']"}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ctb']