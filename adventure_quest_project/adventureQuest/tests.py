from django.test import TestCase
from adventureQuest.models import Post, UserProfile, Quest, Riddle, UserScores
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import datetime
from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.encoding import force_text
import os

#############################################
#   This is our tests for Adventure Quest   #
#############################################


# Helper method to add a user to database.
def add_user(username, email):
    u = User.objects.get_or_create(username=username, email=email)[0]
    u.save()
    u.set_password('123456')
    u.save()
    p = UserProfile.objects.get_or_create(user=u)
    return u


# Helper method to add a quest to database.
def add_quest(name):
    q = Quest.objects.get_or_create(name=name)[0]
    q.description = 'this is a test'
    q.difficulty = 1
    q.age_limit = 4
    q.start_point = 'here'
    q.save()
    return q


# Helper method to add users high score to a quest to the database.
def add_user_scores(user, quest, score):
    us = UserScores.objects.get_or_create(user=user,quest=quest)[0]
    us.score = score
    us.save()
    return us


# Helper method to add a post to database.
def add_post(u, quest, title, content, hints):
    path = os.path.abspath('cat.jpg')
    path = path[:3]
    p = Post.objects.get_or_create(user=u,quest=quest,title = title, image = SimpleUploadedFile(name='cat.jpg', content=open(path+'cat.jpg').read()))[0]
    p.content = content
    p.hints = hints
    p.height_field = 10
    p.width_field = 10
    p.updated = timezone.now()
    p.timestamp = timezone.now()
    p.save()
    return p


# Helper method to add a riddle to the database.
def add_riddle():
    r = Riddle.objects.get_or_create(question_id=0)[0]
    r.question = "hfdjhfdj"
    r.answer= "test"
    r.instruction="sdhsj"
    r.hint ="flkml"
    r.quest_name='city_centre_quest'
    r.save()
    return r


##############################
#   This is our test class   #
##############################
class AdventureQuestTests(TestCase):

    # This tests the hall of fame post functionality.
    def test_hall_of_fame_post(self):
        # Create a new user.
        u = add_user('test','test@adventurequest.com')
        # Create a new Quest.
        q = add_quest('mystery_quest')

        # Create Two posts to test that they are both displayed.
        pOne = add_post(u, q, "Test", "Testing", 1)
        pTwo = add_post(u, q, "BigG", "Had a great time", 2)

        # Create post with default hint value to check that correct message is displayed
        pThree =  add_post(u, q, "Kirsten", "Is smelly", 10000)

        # Access page where posts will be displayed
        response = self.client.get(reverse('mystery_quest_hall_of_fame'))

        # Tests to see whether the information from first two posts is displayed
        self.assertIn('Test'.lower(), response.content.lower())
        self.assertIn('BigG'.lower(), response.content.lower())
        self.assertIn('Testing'.lower(), response.content.lower())
        self.assertIn('Had a great time'.lower(), response.content.lower())
        self.assertIn('1'.lower(), response.content.lower())
        self.assertIn('2'.lower(), response.content.lower())

        # Test to see if correct message is displayed when user makes a post before completing the quest.
        self.assertIn('is still to conquer this quest'.lower(), response.content.lower())

    # Test to see that correct links/messages are displayed when user is logged in.
    def test_pages_while_logged_in(self):
        # Create a new user.
        u = add_user('test', 'test@adventurequest.com')
        # Log user in.
        self.client.post(reverse('login'), {'username':'test', 'password':'123456'})
        # Test user is looged in successfully.
        self.assertEqual(int(self.client.session['_auth_user_id']), u.pk)

        # Access index page.
        response = self.client.get(reverse('index'))

        # Test that messages that should be displayed when user is logged in are displayed.
        self.assertIn('My Account'.lower(), response.content.lower())
        self.assertIn('Logout'.lower(), response.content.lower())

    # Test to see that correct links/messages are not displayed if user not logged in.
    def test_pages_while_logged_out(self):
        # Access index page.
        response = self.client.get(reverse('index'))

        # Test that logout and my account are not available if user is not logged in.
        self.assertNotIn('My Account'.lower(), response.content.lower())
        self.assertNotIn('Logout'.lower(), response.content.lower())

    # Test to see that when you complete a Quest the number of hints you used is saved and
    # displayed on the my account page.
    def test_my_account_save_hints(self):
        # Create a new user.
        u = add_user('test', 'test@adventurequest.com')
        # Create a new quest.
        q = add_quest('city_centre_quest')
        # Create a high score for user u on test q.
        us = add_user_scores(u,q,5)
        # log user in.
        self.client.post(reverse('login'), {'username': 'test', 'password': '123456'})

        # Access my account page.
        response = self.client.get(reverse('my_account'))

        # Test if user score is displayed on my account page.
        self.assertIn('5'.lower(), response.content.lower())

    # Test to check that the quest about pages contain information about the right quest.
    def test_check_quest_abouts(self):
        # Create all the quests.
        c = add_quest('city_centre_quest')
        m = add_quest('mystery_quest')
        f = add_quest('finnieston_quest')
        s = add_quest('southside_quest')
        g = add_quest('glasgow_uni_quest')
        k = add_quest('kids_quest')

        # Test the city centre about page contains the correct information
        response = self.client.get(reverse('city_centre_about'))
        self.assertIn('City Centre'.lower(), response.content.lower())

        # Test the mystery about page contains the correct information
        response = self.client.get(reverse('mystery_about'))
        self.assertIn('Mystery'.lower(), response.content.lower())

        # Test the finnieston about page contains the correct information
        response = self.client.get(reverse('finnieston_about'))
        self.assertIn('Finnieston'.lower(), response.content.lower())

        # Test the southside about page contains the correct information
        response = self.client.get(reverse('southside_about'))
        self.assertIn('Southside'.lower(), response.content.lower())

        # Test the glasgow university about page contains the correct information
        response = self.client.get(reverse('glasgow_uni_about'))
        self.assertIn('university'.lower(), response.content.lower())

        # Test the kids about page contains the correct information
        response = self.client.get(reverse('kids_about'))
        self.assertIn('kidz'.lower(), response.content.lower())






