from django.db import models
from datetime import datetime
# Create your models here.


class Tags(models.Model):
    """
    This class has many to many relatons with content for tags eg: "music", "sport", "food"
    """
    title = models.CharField(max_length=20)


class Source(models.Model):
    """
    This class help us in tracking a source (url) for article sync contineously.
    """
    url = models.CharField(max_length=200)
    last_sync = models.DateTimeField(default=datetime.now())




class Content(models.Model):
    """
    This class stores all the content with basic details
    """
    title = models.CharField(max_length=50)
    content = models.TextField()
    tags = models.ManyToManyField(Tags, db_index=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Media(models.Model):
    """
    This class stores all the media file for certain article eg: video, picture, audio
    """
    type = models.CharField(max_length=10)
    url = models.CharField(max_length=200)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)



