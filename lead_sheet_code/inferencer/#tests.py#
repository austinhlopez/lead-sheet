"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django.test.client import RequestFactory

from inferencer.models import Word, Genre, Topic, Artist, Track

###################  Word Tests ##########################

#class WordModelTests(TestCase):  
    #TODO: Move functions in test_create to check whether 
    #special cases (i.e., a space in Word.name) are handled 
    #correctly.
''' # name has space in it. Do not create. Resulting object 
        # list should still have count 0.
        Word.objects.create(name='glop py', count=0)
        response = ListWordView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 0)
        
        # negative count. Do not create/throw error.
        Word.objects.create(name='Gliffy', count=-1)
        response = ListWordView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 0)'''

"""NOTE: Unit testing is super important. Which tests should be in place?"""


# These tests only make sure that ListWordView correctly
# lists all of the words that have been added thus far.
class ListWordViewTests(TestCase):
    """Word list view tests"""
    # What kind of tests do I need to make when adding words?
    
    # make sure the word name:
    # Doesn't have spaces
    # Check any markdown/potential problems with characters in 
    # databases (POSTGRES stuff)
    def test_words_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        # Is this word properly displayed?
        Word.objects.create(name="bird", count=300)
        response = ListWordView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
        

#################### Artist Tests ########################

#class ArtistModelTests(TestCase):
    # What kind of limits on artist variables should I consider?
    # (Look up typical testing procedures)
    
    # Make sure Artist name
    # Doesn't PREVENT spaces.
'''def test_artists_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        # name has space in it. Do not create. Resulting object 
        # list should still have count 0.
        Artist.objects.create()
        response = ListWordView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 0)
        
        # negative count. Do not create/throw error.
        Word.objects.create(name='Gliffy', count=-1)
        response = ListWordView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 0)    '''


class ListArtistView(TestCase):
    def test_artists_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        # Is this word properly displayed?
        Artist.objects.create(name="Sly & The Family Stone")
        response = ListArtistView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
#################### Genre Tests ##########################

#class GenreModelTests(TestCase):
    

class ListGenreView(TestCase):
    def test_genres_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        # Is this word properly displayed?
        Genre.objects.create(name="Horrorcore")
        response = ListGenreView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
    
#################### Topic Tests ##########################

#class TopicModelTests(TestCase):

class ListTopicView(TestCase):
    def test_topics_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        # Is this word properly displayed?
        Topic.objects.create(name="Food")
        response = ListTopicView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)

#################### Track Tests ##########################

class TrackModelTests(TestCase):
    def test_tracks_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')

        # Is this word properly displayed?
        Track.objects.create(name="Seven Nation Army")
        response = ListTrackView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
