from django import forms
from django.contrib.auth.models import User
from adventureQuest.models import UserProfile


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
class Riddle(forms.ModelForm):
    answer = forms.CharField(max_length=128, help_text="It cannot be seen, cannot be felt, +\n"
                                                       "Cannot be heard, cannot be smelt.+\n"
                                                       "It lies behind stars and under hills,+\n"
                                                       "And empty holes it fills.+\n"
                                                       "It comes out first and follows after,+\n"
                                                       "Ends life, kills laughter. ")