from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #  website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define unicode too!
    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Riddle(models.Model):

    riddleOne = models.CharField(max_length=128)
    riddleTwo = models.CharField(max_length=128)

    def __str__(self):
        return self.riddleOne

    def __unicode__(self):
        return self.riddleTwo

# Model for comments
class Comment(models.Model):

	#needs a foreign key
	#onPage = models.ForeignKey('adventureQuest.Riddle', related_name='comments')
	author = models.CharField(max_length=128)
	text = models.TextField()
	created_date = models.DateTimeField(default=datetime.now)
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.text

	def __unicode__(self):
		return self.text	