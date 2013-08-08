from django.db import models

class Word(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(
        unique=True,
        max_length=60,
        )
    
    count = models.IntegerField(
        )

    def __unicode__(self):
        return self.name

class Genre(models.Model):
    # This will be important, eventually...
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(
        unique=True,
        max_length=120,
        )

    # Number of tracks associated with this tag.
    count = models.IntegerField(
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
        unique=True,
        blank=True,
        null=True,
        default="",
    ) #Note: name can be added after the fact

    topic_words = models.ManyToManyField(
        Word, 
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
        max_length=255,
        )

    msd_id = models.CharField(
        unique=True,
        max_length=30,
        blank = True,
        null = True,
        default = None,
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
    
    # TODO: Replace region_cluster with a Region model.
    # Allow naming of certain region, etc. etc.
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

    location = models.CharField(
        max_length=100,
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
        through = 'ArtistTopic',
        blank=True,
        null=True,
        )

    # To do: Make Artist inherit metadata from any tracks
    # belonging to it, and vice-versa.
    def __unicode__(self):
        return self.name

    # Returns a list of topics, formatted to be used in 
    # a highcharts piechart.
    def get_topics_for_chart(self):
        
        # Keep track of track_count in order to normalize topic 
        # distributions for each and incorporate them into the 
        # total artist distribution.
        track_count = 0
        topic_dict = {}
        for track in self.tracks.all():
            track_count += 1
            for tracktopic in track.tracktopic_set.all():
                topic_id = tracktopic.topic.id
                proportion = tracktopic.topic_proportion
                if topic_id not in topic_dict.keys():
                    topic_dict[topic_id] = proportion
                else:
                    topic_dict[topic_id] += proportion
        # Normalize proportions in topic_dict by the number of
        # total tracks considered, remove low-scoring tracks.
                    
        data_json = "data: ["
                    
        count = 0
        for topic_id, proportion in topic_dict.iteritems():
            new_proportion = proportion/track_count
            topic_dict[topic_id] = new_proportion
            count += topic_dict[topic_id]

            formatted_element = "['%d', %0.2f],\n" % (topic_id, topic_dict[topic_id])
            data_json += formatted_element
        leftover = 1 - count
        data_json += "['other', %0.2f]\n]" % leftover
        
        return data_json


#TODO: Include MSD track_id as a field. Goes for artist, too.
class Track(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    
    name = models.CharField(
        max_length=255,
    )

    #What is the ACTUAL length of these id's?
    msd_id = models.CharField(
        max_length=30,
        unique = True,
        blank = True,
        null = True,
        default = None,
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
                
    STATUS = (
        ('I', 'Included'), #included in current topic analysis.
        ('C', 'Confirmed'), #track info is confirmed, but not analyzed.
        ('U', 'Unverified'),#possibly incorrect/redundant
    )

    track_status = models.CharField(
        max_length = 1,
        choices=STATUS,
        default='U',
        blank=True,
        )
    
    topics = models.ManyToManyField(
        Topic,
        through = 'TrackTopic',
        blank=True,
        null=True,
        )

    class Meta:
        unique_together = ("name", "artist")
    
    def __unicode__(self):
        return self.name
                  
    # Returns a list of topics, formatted to be used 
    # in a highcharts piechart.
    def get_topics_for_chart(self):
        count = 0
        
        data_json = "data: ["

        for tracktopic in self.tracktopic_set.all():
            count += tracktopic.topic_proportion
            formatted_element = "['%d', %0.2f],\n" % (tracktopic.topic.id, tracktopic.topic_proportion)
            data_json += formatted_element
            
        
        leftover = 1 - count
        data_json += "['other', %0.2f]\n]" % leftover      
        return data_json

    #This is probably the wrong place for this?
    def get_topicwords_for_chart(self):
        for tracktopic in self.tracktopic_set.all():
            topic_id = tracktopic.topic.id
            top_words_query = tracktopic.topic.topicword_set.all().filter(position__lte = 10)

            return top_words_query
                        

class TopicWord(models.Model):
    topic = models.ForeignKey(Topic)
    word = models.ForeignKey(Word)
    position = models.IntegerField(
        blank=True,
        null=True
        )
    count = models.IntegerField(
        blank=True,
        null=True
        )
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
        blank=True,
        null=True,
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
        blank=True,
        null=True,
        )
    
    class Meta:
        unique_together = ("artist", "topic")

class ArtistGenre(models.Model):
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre, to_field='name', max_length=120)

    genre_position = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Is this the primary genre listing?",
        )

    class Meta:
        unique_together = ("artist", "genre")
