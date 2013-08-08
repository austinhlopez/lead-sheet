from django.conf.urls import patterns, include, url
from haystack.views import SearchView

from inferencer import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    'inferencer.views',
    # Examples:
    # url(r'^$', 'lead_sheet_code.views.home', name='home'),
    # url(r'^lead_sheet_code/', include('lead_sheet_code.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # List url's
    url(r'^$', 
        SearchView(
            template="home.html",
            results_per_page=10,),
        name="home"),
    url(r'^api$', 'api_root'),

    url(r'^words/$', 
        views.WordList.as_view(),
        name='word-list'),
    
    url(r'^artists/$', 
        views.ArtistList.as_view(),
        name='artist-list'),
    url(r'^artists/(?P<pk>[0-9]+)/$',
        views.ArtistDetail.as_view(),
        name='artist-detail'),
    url(r'^artists/stats/(?P<pk>[0-9]+)/$',
        views.ArtistStats.as_view(template_name = "artist_stats.html"),
        name='artist-stats'),


    url(r'^genres/$', 
        views.GenreList.as_view(),
        name='genre-list'),
    url(r'^genres/(?P<pk>[0-9]+)/$', 
        views.GenreDetail.as_view(),
        name='genre-detail'),

    url(r'^topics/$', 
        views.TopicList.as_view(),
        name='topic-list'),
    url(r'^topics/(?P<pk>[0-9]+)$', 
        views.TopicDetail.as_view(),
        name='topic-detail'),

    url(r'^tracks/$', 
        views.TrackList.as_view(),
        name='track-list'),
    url(r'^tracks/(?P<pk>[0-9]+)/$', 
        views.TrackDetail.as_view(),
        name='track-detail'),
    url(r'^tracks/stats/(?P<pk>[0-9]+)/$',
        views.TrackStats.as_view(template_name = "track_stats.html"),
        name='track-stats'),

    url(r'^topic-words/$', 
        views.TopicWordList.as_view(),
        name='topic-word-list'),

    url(r'^track-topics/$', 
        views.TrackTopicList.as_view(),
        name='track-topic-list'),
    
    url(r'^artist-topics/$',
        views.ArtistTopicList.as_view(),
        name='artist-topic-list'),

    url(r'^artist-genres/$', 
        views.ArtistGenreList.as_view(),
        name='artist-genre-list'),
)
