# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Genre.name'
        db.alter_column(u'inferencer_genre', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=120))

    def backwards(self, orm):

        # Changing field 'Genre.name'
        db.alter_column(u'inferencer_genre', 'name', self.gf('django.db.models.fields.CharField')(max_length=60, unique=True))

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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
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