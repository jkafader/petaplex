from django.db import models
from jsonfield import JSONField

# Create your models here.
class Film(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=600)
    plot = models.TextField()
    rating = models.FloatField()
    is_porn = models.BooleanField()
    collect = models.BooleanField()
    admin_notes = models.TextField()
    collection = models.CharField(max_length=200)
    ia_item_id = models.TextField()
    imdb_id = models.CharField(max_length=200, unique=True)

class VideoItem(models.Model):
    film = models.ForeignKey('Film', null=True, blank=True)
    resolution = models.IntegerField()
    size = models.BigIntegerField()
    ia_metadata = JSONField()
    def save(self, *args, **kwargs):
        # create or find associated film
        # set foreign key
        self.film = Film.objects.get_or_create(
            year=self.ia_metadata.get('omdb', {}).get('Year'),
            title=self.ia_metadata.get('omdb', {}).get('Title'),
            imdb_id=self.ia_metadata.get('metadata', {}).get('external-identifier'),
            )
        # set resolution
        self.resolution=self.ia_metadata.get('')
        # set size
        self.size=self.ia_metadata.get('')
        super().save(*args, **kwargs)
