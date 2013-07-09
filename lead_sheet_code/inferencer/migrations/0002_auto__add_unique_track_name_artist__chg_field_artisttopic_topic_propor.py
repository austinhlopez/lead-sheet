# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Track', fields ['name', 'artist']
        db.create_unique(u'inferencer_track', ['name', 'artist_id'])


        # Changing field 'ArtistTopic.topic_proportion'
        db.alter_column(u'inferencer_artisttopic', 'topic_proportion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=3))
        # Adding unique constraint on 'ArtistTopic', fields ['topic', 'artist']
        db.create_unique(u'inferencer_artisttopic', ['topic_id', 'artist_id'])

        # Adding unique constraint on 'Topic', fields ['name']
        db.create_unique(u'inferencer_topic', ['name'])


        # Changing field 'ArtistGenre.genre_position'
        db.alter_column(u'inferencer_artistgenre', 'genre_position', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding unique constraint on 'ArtistGenre', fields ['genre', 'artist']
        db.create_unique(u'inferencer_artistgenre', ['genre_id', 'artist_id'])


        # Changing field 'TrackTopic.topic_proportion'
        db.alter_column(u'inferencer_tracktopic', 'topic_proportion', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=3))
        # Adding unique constraint on 'TrackTopic', fields ['track', 'topic']
        db.create_unique(u'inferencer_tracktopic', ['track_id', 'topic_id'])


        # Changing field 'TrackGenre.genre_position'
        db.alter_column(u'inferencer_trackgenre', 'genre_position', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding unique constraint on 'TrackGenre', fields ['track', 'genre']
        db.create_unique(u'inferencer_trackgenre', ['track_id', 'genre_id'])

        # Adding field 'TopicWord.count'
        db.add_column(u'inferencer_topicword', 'count',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'TopicWord.position'
        db.alter_column(u'inferencer_topicword', 'position', self.gf('django.db.models.fields.IntegerField')(null=True))
        # Adding unique constraint on 'TopicWord', fields ['topic', 'word']
        db.create_unique(u'inferencer_topicword', ['topic_id', 'word_id'])

        # Adding unique constraint on 'TopicWord', fields ['topic', 'position']
        db.create_unique(u'inferencer_topicword', ['topic_id', 'position'])


    def backwards(self, orm):
        # Removing unique constraint on 'TopicWord', fields ['topic', 'position']
        db.delete_unique(u'inferencer_topicword', ['topic_id', 'position'])

        # Removing unique constraint on 'TopicWord', fields ['topic', 'word']
        db.delete_unique(u'inferencer_topicword', ['topic_id', 'word_id'])

        # Removing unique constraint on 'TrackGenre', fields ['track', 'genre']
        db.delete_unique(u'inferencer_trackgenre', ['track_id', 'genre_id'])

        # Removing unique constraint on 'TrackTopic', fields ['track', 'topic']
        db.delete_unique(u'inferencer_tracktopic', ['track_id', 'topic_id'])

        # Removing unique constraint on 'ArtistGenre', fields ['genre', 'artist']
        db.delete_unique(u'inferencer_artistgenre', ['genre_id', 'artist_id'])

        # Removing unique constraint on 'Topic', fields ['name']
        db.delete_unique(u'inferencer_topic', ['name'])

        # Removing unique constraint on 'ArtistTopic', fields ['topic', 'artist']
        db.delete_unique(u'inferencer_artisttopic', ['topic_id', 'artist_id'])

        # Removing unique constraint on 'Track', fields ['name', 'artist']
        db.delete_unique(u'inferencer_track', ['name', 'artist_id'])


        # Changing field 'ArtistTopic.topic_proportion'
        db.alter_column(u'inferencer_artisttopic', 'topic_proportion', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=3))

        # Changing field 'ArtistGenre.genre_position'
        db.alter_column(u'inferencer_artistgenre', 'genre_position', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'TrackTopic.topic_proportion'
        db.alter_column(u'inferencer_tracktopic', 'topic_proportion', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=3, decimal_places=3))

        # Changing field 'TrackGenre.genre_position'
        db.alter_column(u'inferencer_trackgenre', 'genre_position', self.gf('django.db.models.fields.IntegerField')(default=0))
        # Deleting field 'TopicWord.count'
        db.delete_column(u'inferencer_topicword', 'count')


        # Changing field 'TopicWord.position'
        db.alter_column(u'inferencer_topicword', 'position', self.gf('django.db.models.fields.IntegerField')(default=0))

    models = {
        u'inferencer.artist': {
            'Meta': {'object_name': 'Artist'},
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inferencer.Genre']", 'null': 'True', 'through': u"orm['inferencer.ArtistGenre']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'region_cluster': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inferencer.Topic']", 'null': 'True', 'through': u"orm['inferencer.ArtistTopic']", 'blank': 'True'}),
            'years_active_end': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'years_active_start': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'inferencer.artistgenre': {
            'Meta': {'unique_together': "(('artist', 'genre'),)", 'object_name': 'ArtistGenre'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Artist']"}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Genre']"}),
            'genre_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inferencer.artisttopic': {
            'Meta': {'unique_together': "(('artist', 'topic'),)", 'object_name': 'ArtistTopic'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Topic']"}),
            'topic_proportion': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '3', 'decimal_places': '3', 'blank': 'True'})
        },
        u'inferencer.genre': {
            'Meta': {'object_name': 'Genre'},
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
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inferencer.Genre']", 'null': 'True', 'through': u"orm['inferencer.TrackGenre']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'unique': 'True', 'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region_cluster': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'topics': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['inferencer.Topic']", 'null': 'True', 'through': u"orm['inferencer.TrackTopic']", 'blank': 'True'}),
            'track_status': ('django.db.models.fields.CharField', [], {'default': "('U', 'Unverified')", 'max_length': '1', 'blank': 'True'}),
            'year_released': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'inferencer.trackgenre': {
            'Meta': {'unique_together': "(('track', 'genre'),)", 'object_name': 'TrackGenre'},
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Genre']"}),
            'genre_position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'track': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inferencer.Track']"})
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