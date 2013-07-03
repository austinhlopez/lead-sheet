# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Word'
        db.create_table(u'inferencer_word', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inferencer', ['Word'])

        # Adding model 'Genre'
        db.create_table(u'inferencer_genre', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal(u'inferencer', ['Genre'])

        # Adding model 'Topic'
        db.create_table(u'inferencer_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'inferencer', ['Topic'])

        # Adding model 'Artist'
        db.create_table(u'inferencer_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('years_active_start', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('years_active_end', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('region_cluster', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'inferencer', ['Artist'])

        # Adding model 'Track'
        db.create_table(u'inferencer_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Artist'], null=True, blank=True)),
            ('year_released', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('region_cluster', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('track_status', self.gf('django.db.models.fields.CharField')(default=('U', 'Unverified'), max_length=1, blank=True)),
        ))
        db.send_create_signal(u'inferencer', ['Track'])

        # Adding model 'TopicWord'
        db.create_table(u'inferencer_topicword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Topic'])),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Word'])),
            ('position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inferencer', ['TopicWord'])

        # Adding model 'TrackTopic'
        db.create_table(u'inferencer_tracktopic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Track'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Topic'])),
            ('topic_proportion', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=3)),
        ))
        db.send_create_signal(u'inferencer', ['TrackTopic'])

        # Adding model 'ArtistTopic'
        db.create_table(u'inferencer_artisttopic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Artist'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Topic'])),
            ('topic_proportion', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=3)),
        ))
        db.send_create_signal(u'inferencer', ['ArtistTopic'])

        # Adding model 'TrackGenre'
        db.create_table(u'inferencer_trackgenre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Track'])),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Genre'])),
            ('genre_position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inferencer', ['TrackGenre'])

        # Adding model 'ArtistGenre'
        db.create_table(u'inferencer_artistgenre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Artist'])),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Genre'])),
            ('genre_position', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inferencer', ['ArtistGenre'])


    def backwards(self, orm):
        # Deleting model 'Word'
        db.delete_table(u'inferencer_word')

        # Deleting model 'Genre'
        db.delete_table(u'inferencer_genre')

        # Deleting model 'Topic'
        db.delete_table(u'inferencer_topic')

        # Deleting model 'Artist'
        db.delete_table(u'inferencer_artist')

        # Deleting model 'Track'
        db.delete_table(u'inferencer_track')

        # Deleting model 'TopicWord'
        db.delete_table(u'inferencer_topicword')

        # Deleting model 'TrackTopic'
        db.delete_table(u'inferencer_tracktopic')

        # Deleting model 'ArtistTopic'
        db.delete_table(u'inferencer_artisttopic')

        # Deleting model 'TrackGenre'
        db.delete_table(u'inferencer_trackgenre')

        # Deleting model 'ArtistGenre'
        db.delete_table(u'inferencer_artistgenre')


    models = {
        u'inferencer.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'region_cluster': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'years_active_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'years_active_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'inferencer.artistgenre': {
            'Meta': {'object_name': 'ArtistGenre'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Artist']"}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Genre']"}),
            'genre_position': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inferencer.artisttopic': {
            'Meta': {'object_name': 'ArtistTopic'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Topic']"}),
            'topic_proportion': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '3'})
        },
        u'inferencer.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'inferencer.topic': {
            'Meta': {'object_name': 'Topic'},
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'inferencer.topicword': {
            'Meta': {'object_name': 'TopicWord'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Topic']"}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Word']"})
        },
        u'inferencer.track': {
            'Meta': {'object_name': 'Track'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Artist']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region_cluster': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'track_status': ('django.db.models.fields.CharField', [], {'default': "('U', 'Unverified')", 'max_length': '1', 'blank': 'True'}),
            'year_released': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'inferencer.trackgenre': {
            'Meta': {'object_name': 'TrackGenre'},
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Genre']"}),
            'genre_position': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Track']"})
        },
        u'inferencer.tracktopic': {
            'Meta': {'object_name': 'TrackTopic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Topic']"}),
            'topic_proportion': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '3'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Track']"})
        },
        u'inferencer.word': {
            'Meta': {'object_name': 'Word'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        }
    }

    complete_apps = ['inferencer']