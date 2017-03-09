from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
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
    question = models.CharField(max_length=128)
    answer = models.CharField(max_length = 128)
    quest_name = models.CharField(max_length=128)
    question_id = models.IntegerField(0)

    def __str__(self):
        return self.question

    def __unicode__(self):
        return self.question

    def __str__(self):
        return self.answer

    def __unicode__(self):
        return self.answer

    def __str__(self):
        return self.id

    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.question_id

    def __unicode__(self):
        return self.question_id


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


#Quest
class Quest(models.Model):
    #post = models.ForeignKey(Post)
    description = models.TextField()
    difficulty = models.CharField(max_length=120)
    age_limit = models.IntegerField()

    def __str__(self):
        return self.description

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.difficulty

    def __unicode__(self):
        return self.difficulty

    def __str__(self):
        return self.age_limit

    def __unicode__(self):
        return self.age_limit



# Post to upload images
class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="heigth_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

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