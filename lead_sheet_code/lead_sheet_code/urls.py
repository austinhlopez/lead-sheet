from django.conf.urls import patterns, include, url
from inferencer import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'lead_sheet_code.views.home', name='home'),
    # url(r'^lead_sheet_code/', include('lead_sheet_code.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # List url's
    url(r'^words/$', views.WordList.as_view()),
    
    url(r'^artists/$', views.ArtistList.as_view()),
    url(r'^artists/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view()),

    url(r'^genres/$', views.GenreList.as_view()),

    url(r'^topics/$', views.TopicList.as_view()),

    url(r'tracks/$', views.TrackList.as_view()),
    url(r'^tracks/(?P<pk>[0-9]+)/$', views.TrackDetail.as_view()),
)
