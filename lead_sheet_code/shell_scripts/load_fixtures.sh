#/bin/bash

py ../manage.py loaddata ../../fixtures/artists.json
py ../manage.py loaddata ../../fixtures/genres.json
py ../manage.py loaddata ../../fixtures/topics.json
py ../manage.py loaddata ../../fixtures/tracks.json
py ../manage.py loaddata ../../fixtures/words.json
py ../manage.py loaddata ../../fixtures/artist_genres.json
py ../manage.py loaddata ../../fixtures/track_topics.json
py ../manage.py loaddata ../../fixtures/topic_words.json