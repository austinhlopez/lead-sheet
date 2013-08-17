# Create your views here.
from inferencer.models import Word, Artist, Genre, Topic, Track, TopicWord, TrackTopic, ArtistTopic, ArtistGenre

from inferencer.serializers import ArtistSerializer, TrackSerializer, WordSerializer, GenreSerializer, TopicSerializer, TopicWordSerializer, TrackTopicSerializer, ArtistTopicSerializer, ArtistGenreSerializer

from django.views.generic import View, DetailView, TemplateView

from rest_framework import generics
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.reverse import reverse
from rest_framework.views import APIView

######## API Endpoint #######

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
            'words': reverse('word-list', request=request, format=format),
            'artists': reverse('artist-list', request=request, format=format),
            'genres': reverse('genre-list', request=request, format=format),
            'topics': reverse('topic-list', request=request, format=format),
            'tracks': reverse('track-list', request=request, format=format),
            'topic-words': reverse('topic-word-list', request=request, format=format),
            'track-topics': reverse('track-topic-list', request=request, format=format),
            'artist-topics': reverse('artist-topic-list', request=request, format=format),
            'artist-genres': reverse('artist-genre-list', request=request, format=format)
            })

# Later: modify permissions
# and things so that creation/
# destruction/updating the API
# is ADMIN ONLY.

####### Home View #########
class Home(TemplateView):
    """
    The View you see on arriving to the website.
    """
    template_name = 'home.html'

######## Word Views #########

class WordList(generics.ListCreateAPIView):
    """ 
    List all words, or create new word.
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    paginate_by = 100

    # get and post methods pre-written in ListCreateAPIView

######## Artist Views #########

class ArtistList(generics.ListCreateAPIView):
    """
    List all Artists, or create a new artist.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    paginate_by = 30

class ArtistDetail(DetailView):
    """
    Retrieve, update or delete an artist instance.
    """
    model = Artist
    template_name = "artist_detail.html"

class ArtistStats(DetailView):
    model = Artist 
    template_name = "artist_stats.html"

#GET, PUT, POST, and DELETE handled in the RetrieveUpdate...etc view
######## Genre Views #########

class GenreList(generics.ListCreateAPIView):
    """
    List all Genres, or create a new genre.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    paginate_by = 100

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an artist instance.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

######## Topic Views #########

class TopicList(generics.ListCreateAPIView):
    """
    List all Topics, or create a new topic.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    paginate_by = 100

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List details for one topic.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    

######## Track Views #########

class TrackList(generics.ListCreateAPIView):
    """
    List all Tracks, or create a new track.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    paginate_by = 30

class TrackDetail(DetailView):
    """
    Retrieve, update or delete an artist instance.
    """
    model = Track 
    template_name="track_detail.html"

class TrackStats(DetailView):
    model = Track
    template_name="track_stats.html"

    

######### TopicWord Views #########
class TopicWordList(generics.ListCreateAPIView):
    """
    List all TopicWord relations, or create a new one.
    """
    queryset = TopicWord.objects.all()
    serializer_class = TopicWordSerializer
    paginate_by = 100

######## TrackTopic Views ###########
class TrackTopicList(generics.ListCreateAPIView):
    """
    List all TrackTopic relations, or create a new one.
    """
    queryset = TrackTopic.objects.all()
    serializer_class = TrackTopicSerializer
    paginate_by = 100

######## ArtistTopic Views ###########
class ArtistTopicList(generics.ListCreateAPIView):
    """
    List all ArtistTopic relations, or create a new one.
    """
    queryset = ArtistTopic.objects.all()
    serializer_class = ArtistTopicSerializer
    paginate_by = 100

######## ArtistGenre Views ###########
class ArtistGenreList(generics.ListCreateAPIView):
    """
    List all ArtistGenre relations, or create a new one.
    """
    queryset = ArtistGenre.objects.all()
    serializer_class = ArtistGenreSerializer
    paginate_by = 100


