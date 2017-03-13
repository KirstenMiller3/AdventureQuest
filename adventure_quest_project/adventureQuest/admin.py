from django.contrib import admin
from adventureQuest.models import UserProfile, Comment, Riddle, Quest




# Register your models here.
admin.site.register(UserProfile)

admin.site.register(Comment)

admin.site.register(Riddle)

admin.site.register(Quest)
