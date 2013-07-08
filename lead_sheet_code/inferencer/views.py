# Create your views here.
from inferencer.models import Word, Artist, Genre, Topic, Track
from inferencer.serializers import ArtistSerializer, TrackSerializer, WordSerializer, GenreSerializer, TopicSerializer
from rest_framework import generics


######## Word Views #########

class WordList(generics.ListCreateAPIView):
    """ 
    List all words, or create new word.
    """
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    # get and post methods pre-written in ListCreateAPIView

######## Artist Views #########

class ArtistList(generics.ListCreateAPIView):
    """
    List all Artists, or create a new artist.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an artist instance.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    #GET, PUT, POST, and DELETE handled in the RetrieveUpdate...etc view
######## Genre Views #########

class GenreList(generics.ListCreateAPIView):
    """
    List all Genres, or create a new genre.
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

######## Track Views #########

class TrackList(generics.ListCreateAPIView):
    """
    List all Tracks, or create a new track.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an artist instance.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    #GET, PUT, POST, and DELETE handled in the RetrieveUpdate...etc view
