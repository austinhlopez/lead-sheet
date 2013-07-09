from django.db import models

class Word(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(
        unique=True,
        max_length=60,
        )
    
    count = models.IntegerField(
        verbose_name="Total count of this word within the dataset.",
        )

    def __unicode__(self):
        return self.name

class Genre(models.Model):
    # This will be important, eventually...
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(
        unique=True,
        max_length=60,
        )

    # In the future, I should create some sort of system 
    # for describing genre hierarchies/relationships.
    # A slider, to specify 'specificness' of a genre 
    # designation.
                                    
    def __unicode__(self):
        return self.name

# Create your models here.
class Topic(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(
        max_length=255,
        unique=True
    ) #Note: name can be added after the fact

    topic_words = models.ManyToManyField(
        Word, 
        verbose_name="List of the top words for a given topic",
        through='TopicWord',
        )

    def __unicode__(self):
        return self.name

class Artist(models.Model):
    id = models.AutoField(
        primary_key=True, 
        unique=True,
        )
    name = models.CharField(
        unique=True,
        max_length=255,
        )

    #TODO: Set this up to inherit any appropriate
    #info from track.

    years_active_start = models.IntegerField(
        null=True,
        blank=True,
        )
    
    years_active_end = models.IntegerField(
        blank=True,
        null=True,
        )
    
    region_cluster = models.IntegerField(
        blank=True,
        null=True,
        )
    
    longitude = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        null=True,
        blank=True,
        )
    
    latitude = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        null=True,
        blank=True,
        )
    
    genres = models.ManyToManyField(
        Genre,
        through='ArtistGenre',
        null=True,
        blank=True,
        ) # Maybe make this a list? Genre distribution as well?
    
    topics = models.ManyToManyField(
        Topic,
        verbose_name = 'topic makeup for this artist.',
        through = 'ArtistTopic',
        blank=True,
        null=True,
        )

    # To do: Make Artist inherit metadata from any tracks
    # belonging to it, and vice-versa.
    def __unicode__(self):
        return self.name

class Track(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    
    name = models.CharField(
        max_length=255,
    )

    artist = models.ForeignKey(
        Artist,
        blank=True,
        null=True,
        related_name='tracks'
        )

    #TODO: Update appropriate track info on artist set.

    year_released = models.IntegerField(
        blank=True,
        null=True,
        )
    
    region_cluster = models.IntegerField(
        blank=True,
        null=True,
        )
    
    longitude = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True,
        )
    
    latitude = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        blank=True,
        null=True,
        )
    
    genres = models.ManyToManyField(
        Genre,
        through='TrackGenre',
        blank=True,
        null=True,
        )
        
    STATUS = (
        ('I', 'Included'), #included in current topic analysis.
        ('C', 'Confirmed'), #track info is confirmed, but not analyzed.
        ('U', 'Unverified'),#possibly incorrect/redundant
    )

    track_status = models.CharField(
        max_length = 1,
        verbose_name = "Has the track been included in the analysis?",
        choices=STATUS,
        default=('U', 'Unverified'),
        blank=True,
        )
    
    topics = models.ManyToManyField(
        Topic,
        verbose_name = 'topic makeup for each track.',
        through = 'TrackTopic',
        blank=True,
        null=True,
        )

    class Meta:
        unique_together = ("name", "artist")
    
    def __unicode__(self):
        return self.name
                                                                        
class TopicWord(models.Model):
    topic = models.ForeignKey(Topic)
    word = models.ForeignKey(Word)
    position = models.IntegerField()
    count = models.IntegerField()
    # TODO: Restrict Integers to 
    # a certain number, ensure there are no redundant positions 
    # for a given topic

    class Meta:
        unique_together = (("topic", "word"), ("topic", "position"))

class TrackTopic(models.Model):
    track = models.ForeignKey(Track)
    topic = models.ForeignKey(Topic)

    topic_proportion = models.DecimalField(
        decimal_places=3,
        max_digits=3,
        verbose_name='What percentage of the overall topic makeup is comprised by this topic?',
        )
    
    class Meta:
        unique_together = ("track", "topic")
    #Todo: make sure that the sum of topic distributions is < 1?

class ArtistTopic(models.Model):
    artist = models.ForeignKey(Artist)
    topic = models.ForeignKey(Topic)

    topic_proportion = models.DecimalField(
        decimal_places=3,
        max_digits=3,
        verbose_name='What percentage of the overall topic makeup is comprised by this topic?',
        )
    
    class Meta:
        unique_together = ("artist", "topic")

class TrackGenre(models.Model):
    track = models.ForeignKey(Track)
    genre = models.ForeignKey(Genre)

    genre_position = models.IntegerField(
        verbose_name="Is this the primary genre listing?",
        )

    class Meta:
        unique_together = ("track", "genre")

class ArtistGenre(models.Model):
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre)

    genre_position = models.IntegerField(
        verbose_name="Is this the primary genre listing?",
        )

    class Meta:
        unique_together = ("artist", "genre")
