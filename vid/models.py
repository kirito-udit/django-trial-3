from django.db import models
from embed_video.fields import EmbedVideoField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# MODELS FOR THE "GIVEAWAY SECTION"
class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()


# MODELS FOR PLAYING VIDEOS
class Detail(models.Model):
     image = models.ImageField(upload_to='images')
     des = models.TextField(max_length=200)
     title = models.TextField(max_length=200,null=True)
     vid = models.FileField(upload_to='videos', null=True)
     #subtitle = models.FileField(upload_to='subtitle', null=True)
     likers = models.ManyToManyField(User, related_name = 'likers', blank = True)
     reporters = models.ManyToManyField(User, related_name = 'reporters', blank = True)
     def __str__(self):
         return self.title


class Comment(models.Model):
    content = models.TextField(null=True)
    post = models.ForeignKey(Detail,on_delete=models.CASCADE,related_name='comments')
    date_posted = models.DateTimeField(default=timezone.now)
    approve = models.BooleanField(default=False,null=True)

    def approved(self):
	    self.approve = True
	    self.save()

    

