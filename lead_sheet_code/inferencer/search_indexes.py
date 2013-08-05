from haystack import indexes
from inferencer.models import Track, Artist

class TrackIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    artist = indexes.CharField(model_attr='artist')
    year_released = indexes.IntegerField(model_attr='year_released')
    track_id = indexes.IntegerField(model_attr='id')

    def get_model(self):
        return Track


class ArtistIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    years_active_start = indexes.IntegerField(model_attr='years_active_start')
    years_active_end = indexes.IntegerField(model_attr='years_active_end')
    region_cluster = indexes.IntegerField(model_attr='region_cluster')
    longitude = indexes.DecimalField(model_attr = 'longitude')
    latitude = indexes.DecimalField(model_attr = 'latitude')
    location = indexes.CharField(model_attr = 'location')
    artist_id = indexes.IntegerField(model_attr = 'id')
    #TODO: Add genre as a filterable option.
    
    def get_model(self):
        return Artist










