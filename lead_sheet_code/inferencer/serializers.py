from django.forms import widgets
from rest_framework import serializers
from inferencer.models import Word, Genre, Topic, Artist, Track, TopicWord, TrackTopic, ArtistTopic, ArtistGenre

# Code largely taken from Django REST framework tutorial.

#ModelSerializer: For when your Serializer closely matches
#that of one of your models.
class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word

    #Skip additional methods: for right now, only Track and 
    #Artist will be updated via serialization/deserialization.

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic


# Hyperlink to filtered list of genres associated with 
# a given artist.
class ArtistSerializer(serializers.ModelSerializer):
    tracks = serializers.RelatedField(many=True)

    class Meta:
        model = Artist
        fields=(
            'name', 'years_active_start', 'years_active_end',
            'region_cluster', 'longitude', 'latitude', 'tracks','genres'
            )

    def restore_object(self, attrs, instance=None):
        """
        Create or update new Artist instance, given a dictionary 
        of deserialized field values.
        """

        if instance:
            # Update existing instance.
            instance.name = attrs.get('name', instance.name)
            instance.years_active_start = attrs.get('years_active_start', instance.years_active_start)
            instance.years_active_end = attrs.get('years_active_end', instance.years_active_end)
            

            # NOTE: Duplicate data between track/artist. How 
            # should we resolve these two fields? Is it helpful
            # to have different fields?
            instance.region_cluster = attrs.get('region_cluster', instance.region_cluster)
            instance.longitude = attrs.get('longitude', instance.longitude)
            instance.latitude = attrs.get('latitude', instance.latitude)
            # TODO instance.genres
            # TODO instance.topics

            instance.tracks = attrs.get('tracks', instance.tracks)
            
            return instance

        return Artist(**attrs)

class TrackSerializer(serializers.ModelSerializer):
    # Note: should use RelatedField, or something, (see
    #rest_framework docs) to relate artist and track (and more).0

    class Meta:
        model = Track
 
    def restore_object(self, attrs, instance=None):
        """
        Create or update a new track instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """

        if instance:
            # Update existing instance.
            # Dictionary get() has a second argument, the default
            # if no key is found.
            instance.name = attrs.get('name', instance.name)
            instance.artist = attrs.get('artist', instance.artist)
            instance.year_released = attrs.get('year_released', instance.year_released)
            instance.region_cluster = attrs.get('region_cluster', instance.region_cluster)
            instance.longitude = attrs.get('longitude', instance.longitude)
            instance.latitude = attrs.get('latitude', instance.latitude)
            #TODO instance.genres TODO
            instance.track_status = attrs.get('track_status', instance.track_status)
            #instance.topics TODO
            return instance

        return Track(**attrs)

class TopicWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicWord

    def restore_object(self, attrs, instance=None):
        """
        Create or update a TopicWord, given a dictionary
        of deserialized field values.
        """
        if instance:
            instance.topic = attrs.get('topic', instance.topic)
            instance.word = attrs.get('word', instance.word)
            instance.position = attrs.get('position', instance.position)
            instance.count = attrs.get('count', instance.count)
            return instance

        return TopicWord(**attrs)

class TrackTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackTopic

    def restore_object(self, attrs, instance=None):
        """
        Create or update a TrackTopic, given a dictionary 
        of deserialized field values."""

        if instance:
            instance.track = attrs.get('track', instance.track)
            instance.topic = attrs.get('topic', instance.topic)
            instance.topic_proportion = attrs.get('topic_proportion', instance.topic_proportion)

            return instance

        return TrackTopic(**attrs)

#NOTE: Artist topic shouldn't come into play until a SEPARATE
#Topic Analysis is made using artist. Until then, artistTopic 
#should simply be an aggregate of track topics.
class ArtistTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistTopic

    def restore_object(self, attrs, instance=None):
        """
        Create or update a TrackTopic, given a dictionary 
        of deserialized field values."""

        if instance:
            instance.artist = attrs.get('artist', instance.artist)
            instance.topic = attrs.get('topic', instance.topic)
            instance.topic_proportion = attrs.get('topic_proportion', instance.topic_proportion)
            return instance

        return ArtistTopic(**attrs)

class ArtistGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistGenre

    def restore_object(self, attrs, instance=None):
        """
        Create or update a TrackTopic, given a dictionary 
        of deserialized field values."""

        if instance:
            instance.artist = attrs.get('artist', instance.artist)
            instance.genre = attrs.get('genre', instance.genre)
            instance.genre_position = attrs.get('genre_position', instance.genre_position)

        return ArtistGenre(**attrs)
