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
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'inferencer', ['Genre'])

        # Adding model 'Topic'
        db.create_table(u'inferencer_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal(u'inferencer', ['Topic'])

        # Adding model 'Artist'
        db.create_table(u'inferencer_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('msd_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, unique=True, null=True, blank=True)),
            ('years_active_start', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('years_active_end', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('region_cluster', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'inferencer', ['Artist'])

        # Adding model 'Track'
        db.create_table(u'inferencer_track', (
            ('id', self.gf('django.db.models.fields.AutoField')(unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('msd_id', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, unique=True, null=True, blank=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='tracks', null=True, to=orm['inferencer.Artist'])),
            ('year_released', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('track_status', self.gf('django.db.models.fields.CharField')(default='U', max_length=1, blank=True)),
        ))
        db.send_create_signal(u'inferencer', ['Track'])

        # Adding unique constraint on 'Track', fields ['name', 'artist']
        db.create_unique(u'inferencer_track', ['name', 'artist_id'])

        # Adding model 'TopicWord'
        db.create_table(u'inferencer_topicword', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Topic'])),
            ('word', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Word'])),
            ('position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'inferencer', ['TopicWord'])

        # Adding unique constraint on 'TopicWord', fields ['topic', 'word']
        db.create_unique(u'inferencer_topicword', ['topic_id', 'word_id'])

        # Adding unique constraint on 'TopicWord', fields ['topic', 'position']
        db.create_unique(u'inferencer_topicword', ['topic_id', 'position'])

        # Adding model 'TrackTopic'
        db.create_table(u'inferencer_tracktopic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('track', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Track'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Topic'])),
            ('topic_proportion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=3, blank=True)),
        ))
        db.send_create_signal(u'inferencer', ['TrackTopic'])

        # Adding unique constraint on 'TrackTopic', fields ['track', 'topic']
        db.create_unique(u'inferencer_tracktopic', ['track_id', 'topic_id'])

        # Adding model 'ArtistTopic'
        db.create_table(u'inferencer_artisttopic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Artist'])),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Topic'])),
            ('topic_proportion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=3, blank=True)),
        ))
        db.send_create_signal(u'inferencer', ['ArtistTopic'])

        # Adding unique constraint on 'ArtistTopic', fields ['artist', 'topic']
        db.create_unique(u'inferencer_artisttopic', ['artist_id', 'topic_id'])

        # Adding model 'ArtistGenre'
        db.create_table(u'inferencer_artistgenre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Artist'])),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inferencer.Genre'], to_field='name')),
            ('genre_position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'inferencer', ['ArtistGenre'])

        # Adding unique constraint on 'ArtistGenre', fields ['artist', 'genre']
        db.create_unique(u'inferencer_artistgenre', ['artist_id', 'genre_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ArtistGenre', fields ['artist', 'genre']
        db.delete_unique(u'inferencer_artistgenre', ['artist_id', 'genre_id'])

        # Removing unique constraint on 'ArtistTopic', fields ['artist', 'topic']
        db.delete_unique(u'inferencer_artisttopic', ['artist_id', 'topic_id'])

        # Removing unique constraint on 'TrackTopic', fields ['track', 'topic']
        db.delete_unique(u'inferencer_tracktopic', ['track_id', 'topic_id'])

        # Removing unique constraint on 'TopicWord', fields ['topic', 'position']
        db.delete_unique(u'inferencer_topicword', ['topic_id', 'position'])

        # Removing unique constraint on 'TopicWord', fields ['topic', 'word']
        db.delete_unique(u'inferencer_topicword', ['topic_id', 'word_id'])

        # Removing unique constraint on 'Track', fields ['name', 'artist']
        db.delete_unique(u'inferencer_track', ['name', 'artist_id'])

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

        # Deleting model 'ArtistGenre'
        db.delete_table(u'inferencer_artistgenre')


    models = {
        u'inferencer.artist': {
            'Meta': {'object_name': 'Artist'},
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inferencer.Genre']", 'null': 'True', 'through': u"orm['inferencer.ArtistGenre']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'msd_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region_cluster': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inferencer.Topic']", 'null': 'True', 'through': u"orm['inferencer.ArtistTopic']", 'blank': 'True'}),
            'years_active_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'years_active_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'inferencer.artistgenre': {
            'Meta': {'unique_together': "(('artist', 'genre'),)", 'object_name': 'ArtistGenre'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Artist']"}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Genre']", 'to_field': "'name'"}),
            'genre_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inferencer.artisttopic': {
            'Meta': {'unique_together': "(('artist', 'topic'),)", 'object_name': 'ArtistTopic'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Topic']"}),
            'topic_proportion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '3', 'blank': 'True'})
        },
        u'inferencer.genre': {
            'Meta': {'object_name': 'Genre'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        u'inferencer.topic': {
            'Meta': {'object_name': 'Topic'},
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'topic_words': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['inferencer.Word']", 'through': u"orm['inferencer.TopicWord']", 'symmetrical': 'False'})
        },
        u'inferencer.topicword': {
            'Meta': {'unique_together': "(('topic', 'word'), ('topic', 'position'))", 'object_name': 'TopicWord'},
            'count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Topic']"}),
            'word': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Word']"})
        },
        u'inferencer.track': {
            'Meta': {'unique_together': "(('name', 'artist'),)", 'object_name': 'Track'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tracks'", 'null': 'True', 'to': u"orm['inferencer.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'msd_id': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inferencer.Topic']", 'null': 'True', 'through': u"orm['inferencer.TrackTopic']", 'blank': 'True'}),
            'track_status': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '1', 'blank': 'True'}),
            'year_released': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'inferencer.tracktopic': {
            'Meta': {'unique_together': "(('track', 'topic'),)", 'object_name': 'TrackTopic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Topic']"}),
            'topic_proportion': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '3', 'blank': 'True'}),
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