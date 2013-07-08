# Create your views here.

from django.views.generic import ListView
from django.views.generic import UpdateView

from django.core.urlresolvers import reverse
from django.views.generic import CreateView

from inferencer.models import Word, Artist, Genre, Topic, Track

from inferencer.serializers import ArtistSerializer, TrackSerializer

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
    template_name = 'artist_edit.html'

    # On success, redirect the user here:
    def get_success_url(self):
        return reverse('artist_list')

    def get_context_data(self, **kwargs):
        context = super(CreateArtistView, self).get_context_data(**kwargs)
        context['action'] = reverse('artist_new')

        return context

class UpdateArtistView(UpdateView):
    model = Artist
    template_name = 'artist_edit.html'

    def get_success_url(self):
        return reverse('artist_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateArtistView, self).get_context_data(**kwargs)
        context['action'] = reverse('artist_edit',
                                    kwargs={'pk' : self.get_object().id})

        return context
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
    template_name = 'track_edit.html'

    # On success, redirect the user here:
    def get_success_url(self):
        return reverse('track_list')

    def get_context_data(self, **kwargs):
        context = super(CreateTrackView, self).get_context_data(**kwargs)
        context['action'] = reverse('track_new')

        return context

class UpdateTrackView(UpdateView):
    model = Track
    template_name = 'track_edit.html'

    def get_success_url(self):
        return reverse('track_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateTrackView, self).get_context_data(**kwargs)
        context['action'] = reverse('track_edit',
                                    kwargs={'pk' : self.get_object().id})

        return context
