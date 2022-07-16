from django.db import models

# Create your models here.

class YTData(models.Model):
    '''
    Model for Saving youtube data to db
    '''

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    published_at = models.DateTimeField()
    thumbnail_url_default = models.URLField(max_length=100)
    thumbnail_url_medium = models.URLField(max_length=100)
    thumbnail_url_high = models.URLField(max_length=100)