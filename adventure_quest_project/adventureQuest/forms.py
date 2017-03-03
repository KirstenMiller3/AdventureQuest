from django import forms
from django.contrib.auth.models import User
from adventureQuest.models import UserProfile, Riddle



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture',)


# Obviously riddles coud involve a number or character answer? Maybe always take it as a String to simplify things?
class RiddleForm(forms.ModelForm):
    riddleOne = forms.CharField(max_length=128, help_text="blablabl")
    riddleTwo = forms.CharField(max_length=128, help_text="hiya!")

    class Meta:
        model = Riddle
        fields = ('riddleOne','riddleTwo',)
