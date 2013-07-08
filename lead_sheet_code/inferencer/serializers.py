from django.forms import widgets
from rest_framework import serializers
from inferencer.models import Word, Genre, Topic, Artist, Track

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
            #instance.artist, TODO
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
