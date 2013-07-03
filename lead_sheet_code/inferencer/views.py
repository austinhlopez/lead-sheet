# Create your views here.

from django.views.generic import ListView

from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from inferencer.models import Word, Artist, Genre, Topic, Track


######## Word Views #########

class ListWordView(ListView):
    model = Word
    template_name = 'word_list.html'

######## Artist Views #########

class ListArtistView(ListView):
    model = Artist
    template_name = 'artist_list.html'

class CreateArtistView(CreateView):
    model = Artist
    template_name = 'artist_new.html'

    # On success, redirect the user here:
    def get_success_url(self):
        return reverse('artist_list')

######## Genre Views #########

class ListGenreView(ListView):
    model = Genre
    template_name = 'genre_list.html'

######## Topic Views #########

class ListTopicView(ListView):
    model = Topic
    template_name = 'topic_list.html'

######## Track Views #########

class ListTrackView(ListView):
    model = Track
    template_name = 'track_list.html'

class CreateTrackView(CreateView):
    model = Track
    template_name = 'track_new.html'

    # On success, redirect the user here:
    def get_success_url(self):
        return reverse('track_list')
