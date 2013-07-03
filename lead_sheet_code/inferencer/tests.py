"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django.text.client import RequestFactory


###################  Word Tests ##########################

class WordModelTests(TestCase):  
    #TODO: Move functions in test_create to check whether 
    #special cases (i.e., a space in Word.name) are handled 
    #correctly.


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

        # name has space in it. Do not create. Resulting object 
        # list should still have count 0.
        Word.objects.create(name='glop py', count=0)
        response = ListWordView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 0)
        
        # negative count. Do not create/throw error.
        Word.objects.create(name='Gliffy', count=-1)
        response = ListWordView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 0)
        

#################### Artist Tests ########################

class ArtistModelTests(TestCase):
    # What kind of limits on artist variables should I consider?
    # (Look up typical testing procedures)
    
    # Make sure Artist name
    # Doesn't PREVENT spaces.
    def test_artists_in_context(self):
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
        self.assertEquals(response.context_data['object_list'].count(), 0)
    


class ListArtistView(TestCase):
#################### Genre Tests ##########################

class GenreModelTests(TestCase):

#################### Topic Tests ##########################

class TopicModelTests(TestCase):


#################### Track Tests ##########################

class TrackModelTests(TestCase):
    

