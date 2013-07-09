"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django.test.client import RequestFactory

from inferencer.models import *
from inferencer.views import *

###################  Word Tests ##########################


# These tests only make sure that ListordView correctly
# lists all of the words that have been added thus far. It
# does NOTE test that inputs are protected from inappropriate 
# values.
class WordListTests(TestCase):
    """Word list view tests"""
    # What kind of tests do I need to make when adding words?
    
    # make sure the word name:
    # Doesn't have spaces
    # Check any markdown/potential problems with characters in 
    # databases (POSTGRES stuff)
    def test_words_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        desired_count = 0

        # Is this word properly displayed?
        Word.objects.create(name="bird", count=300)
        response = WordList.as_view()(request)
        desired_count += 1

        self.assertEquals(response.data['count'], desired_count)
        
#################### Artist Tests ########################
class ArtistListTests(TestCase):
    def test_artists_in_context(self):
        factory = RequestFactory()
        request = factory.get('/artists/')

        desired_count = 0

        # Create an artist with just a name.
        Artist.objects.create(name="Sly & The Family Stone")
        desired_count += 1
        
        response = ArtistList.as_view()(request)

        self.assertEquals(response.data['count'], desired_count)

        # Add another artist, this time with more attributes.
        Artist.objects.create(name="Led Zeppelin", 
                              years_active_start=1969, 
                              years_active_end=1979, 
                              region_cluster=1, 
                              longitude=123.12,
                              latitude=68,
                              )
        desired_count += 1
        response = ArtistList.as_view()(request)
        self.assertEquals(response.data['count'], desired_count)

# Still untested: Tagging genres for a given artist, etc.
#################### Genre Tests ##########################    

class GenreListTests(TestCase):
    def test_genres_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        desired_count = 0

        # Is this word properly displayed?
        Genre.objects.create(name="horrorcore")
        desired_count += 1
        response = GenreList.as_view()(request)
        self.assertEquals(response.data['count'], desired_count)


#################### Topic Tests ##########################

#class TopicModelTests(TestCase):

class TopicListTests(TestCase):
    def test_topics_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        desired_count = 0

        # Is this word properly displayed?
        Topic.objects.create(name="Food")
        response = TopicList.as_view()(request)
        desired_count += 1
        self.assertEquals(response.data['count'], desired_count)

#################### Track Tests ##########################

class TrackListTests(TestCase):
    def test_tracks_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        desired_count = 0

        # Is this track properly displayed?
        Track.objects.create(name="Seven Nation Army")
        response = TrackList.as_view()(request)
        desired_count += 1
        self.assertEquals(response.data['count'], desired_count)
