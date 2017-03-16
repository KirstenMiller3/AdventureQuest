from django.contrib import admin
from adventureQuest.models import UserProfile, Comment
from adventureQuest.models import UserProfile, Comment, Post,Riddle, Quest




# Register your models here.
admin.site.register(UserProfile)

admin.site.register(Comment)

admin.site.register(Riddle)
admin.site.register(Post)

admin.site.register(Quest)


