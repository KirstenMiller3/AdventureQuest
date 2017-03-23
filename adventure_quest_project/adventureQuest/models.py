from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import datetime
from django.template.defaultfilters import slugify
import ast



######################
#   Helper methods   #
######################


# This is a helper methods to allow list fields for models
class ListField(models.TextField):

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


# Helper method to create an upload location for image files
def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


##############################################
#   This is our models for Adventure Quest   #
##############################################


# The UserProfile model stores information about each user.
class UserProfile(models.Model):
    # This links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # A profile picture for the user
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


# The Riddle model stores information for each riddle in the quest.
class Riddle(models.Model):
    question = models.CharField(max_length=128)
    answer = ListField()
    instruction = models.CharField(max_length=128, default='No specific instructions available')
    hint = models.CharField(max_length=128, default='No hint available')
    question_id = models.IntegerField(default=0)
    quest_name = models.CharField(max_length=128)

    def __int__(self):
        return self.question_id


# The Quest model stores information about each different quest.
class Quest(models.Model):
    name = models.CharField(max_length=200, default='new Quest')
    description = models.TextField()
    difficulty = models.CharField(max_length=120)
    age_limit = models.IntegerField(default=0)
    start_point = models.CharField(max_length=120, default = 'here')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


# This is a model to represent the user's scores after they've completed a quest
class UserScores(models.Model):
    user = models.ForeignKey(User)
    quest = models.ForeignKey(Quest)
    score = models.IntegerField(default=1000)

    def __str__(self):
        return self.user

    def __unicode__(self):
        return self.user


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
    hints = models.IntegerField(default=10000)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]


# Model for comments
class Comment(models.Model):
    quest = models.ForeignKey(Quest)
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


