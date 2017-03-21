from django import forms
from django.contrib.auth.models import User
from adventureQuest.models import UserProfile, Riddle, Post


# This is the form to get details when users register.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# This form allows us to get a profile picture for a user when they register.
class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('picture',)


# Upload pictures to gallery
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
            "user",
            "quest",
			"title",
			"image",
			"content",
		]