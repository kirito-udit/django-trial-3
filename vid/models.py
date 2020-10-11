from django.db import models
from embed_video.fields import EmbedVideoField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

"""class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	views = models.ManyToManyField(User, related_name='post_views', blank = True)
	likers = models.ManyToManyField(User, related_name = 'likers', blank = True)"""
class Comment(models.Model):
	comment = models.TextField()
	#date_posted = models.DateTimeField(default=timezone.now)
	#author = models.ForeignKey(User, on_delete=models.CASCADE)
	#post = models.ForeignKey(Post, on_delete=models.CASCADE)
	#likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
class Detail(models.Model):
     image = models.ImageField(upload_to='images')
     des = models.TextField(max_length=200)
     title = models.TextField(max_length=200,null=True)
     vid = models.FileField(upload_to='videos', null=True)
     def __str__(self):
         return self.title