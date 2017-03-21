from django.contrib import admin
from adventureQuest.models import UserProfile, Comment
from adventureQuest.models import UserProfile, Comment, Post,Riddle, Quest, UserScores




# Register your models here.
admin.site.register(UserProfile)

admin.site.register(Comment)

admin.site.register(Riddle)
admin.site.register(Post)

admin.site.register(Quest)
admin.site.register(UserScores)



