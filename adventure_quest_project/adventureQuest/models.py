from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



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