from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import datetime
from django.template.defaultfilters import slugify


# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    #  website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    quest1Score = models.IntegerField(default=0)
    quest2Score = models.IntegerField(default=0)
    quest3Score = models.IntegerField(default=0)
    quest4Score = models.IntegerField(default=0)
    quest5Score = models.IntegerField(default=0)
    quest6Score = models.IntegerField(default=0)
    quest7Score = models.IntegerField(default=0)
    quest8Score = models.IntegerField(default=0)
    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define unicode too!
    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Riddle(models.Model):
    question = models.CharField(max_length=128)
    answer = models.CharField(max_length=128)
    instruction = models.CharField(max_length=128, default='No specific instructions available')
    hint = models.CharField(max_length=128, default='No hint available')
    question_id = models.IntegerField()
    quest_name = models.CharField(max_length=128)

    def __int__(self):
        return self.question_id


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


#Quest
class Quest(models.Model):
    #post = models.ForeignKey(Post)
    name = models.CharField(max_length=200, default='new Quest')
    description = models.TextField()
    difficulty = models.CharField(max_length=120)
    age_limit = models.IntegerField()
    start_point = models.CharField(max_length=120, default = 'here')


    # slug = models.SlugField(unique=True)
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.description)
    #
    #     super(Quest, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.description

    def __unicode__(self):
        return self.name




# Post to upload images
class Post(models.Model):
    user = models.ForeignKey(User, default=1)
    quest = models.ForeignKey(Quest)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    #hints = models.ForeignKey
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
        #return reverse('post_create', kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]


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