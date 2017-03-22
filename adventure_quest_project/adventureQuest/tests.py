from django.test import TestCase
from adventureQuest.models import Post, UserProfile, Quest, Riddle, UserScores
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import datetime
from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile
import os

# Create your tests here.
def add_blah(username, email, password):
    u = UserProfile.objects.get_or_create(User)
    u.username = username
    u.email = email
    u.user.set_password(password)
    u.save()
    return u

def add_user(username, email):
    u = User.objects.get_or_create(username=username, email=email)[0]
    u.save()
    u.set_password('123456')
    u.save()
    p = UserProfile.objects.get_or_create(user=u)
    return u

def add_quest(name):
    q = Quest.objects.get_or_create(name=name)[0]
    q.description = 'this is a test'
    q.difficulty = 1
    q.age_limit=4
    q.start_point = 'here'
    q.save()

    return q

def add_UserScores(user, quest, score):
    us = UserScores.objects.get_or_create(user=user,quest=quest)[0]
    us.score = score
    us.save()

    return us


def add_post(u, quest, title,content,hints):
    path = os.path.abspath('cat.jpg')
    path = path[:3]
    p = Post.objects.get_or_create(user=u,quest=quest,title = title, image = SimpleUploadedFile(name='cat.jpg', content=open(path+'cat.jpg').read(), content_type='image/jpeg'),content = content, hints = hints,height_field=50,width_field=50, updated = timezone.now(), timestamp = timezone.now())[0]
    print("**************************"+str(path))
   # p.content = content
    #p.hints = hints
   # p.height_field = 10
   # p.width_field =10
   # p.updated = timezone.now()
    #p.timestamp = timezone.now()
    p.save()
    return p


def add_riddle():
    r = Riddle.objects.get_or_create(question_id=0, question = "hfdjhfdj", answer= "test", instruction="sdhsj", hint ="flkml", quest_name='city_centre_quest')


class AdventureQuestTests(TestCase):


    def test_add_post_something(self):
        """
        fsdg
        """
        u = add_user('test','test@adventurequest.com')
        q = add_quest('mystery_quest')

        pOne = add_post(u, q, "Test", "Testing", 1)
        pTwo = add_post(u, q, "BigG", "Had a great time", 2)

        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test'.lower(), response.content.lower())
        self.assertIn('BigG'.lower(), response.content.lower())
        self.assertIn('Testing'.lower(), response.content.lower())
        self.assertIn('Had a great time'.lower(), response.content.lower())
        self.assertIn('1'.lower(), response.content.lower())
        self.assertIn('2'.lower(), response.content.lower())

        #if Post.objects.all().ordered:
         #   self.assert



    def test_pages_while_logged_in(self):
        u = add_user('test', 'test@adventurequest.com')
        # log input
        self.client.post(reverse('login'), {'username':'test', 'password':'123456'})
        self.assertEqual(int(self.client.session['_auth_user_id']), u.pk)

        response = self.client.get(reverse('index'))
        self.assertIn('My Account'.lower(), response.content.lower())
        self.assertIn('Logout'.lower(), response.content.lower())



    def test_pages_while_logged_out(self):

        response = self.client.get(reverse('index'))
        self.assertNotIn('My Account'.lower(), response.content.lower())
        self.assertNotIn('Logout'.lower(), response.content.lower())


    def test_my_account_save_hints(self):
        u = add_user('test', 'test@adventurequest.com')
        q = add_quest('city_centre_quest')
        us = add_UserScores(u,q,5)

        self.client.post(reverse('login'), {'username': 'test', 'password': '123456'})
        response = self.client.get(reverse('my_account'))
        self.assertIn('5'.lower(), response.content.lower())


    def test_check_quest_abouts(self):
        c = add_quest('city_centre_quest')
        m = add_quest('mystery_quest')
        f = add_quest('finnieston_quest')
        s = add_quest('southside_quest')
        g = add_quest('glasgow_uni_quest')
        k = add_quest('kids_quest')

        response = self.client.get(reverse('city_centre_about'))
        self.assertIn('City Centre'.lower(), response.content.lower())

        response = self.client.get(reverse('mystery_about'))
        self.assertIn('Mystery'.lower(), response.content.lower())

        response = self.client.get(reverse('finnieston_about'))
        self.assertIn('Finnieston'.lower(), response.content.lower())

        response = self.client.get(reverse('southside_about'))
        self.assertIn('Southside'.lower(), response.content.lower())

        response = self.client.get(reverse('glasgow_uni_about'))
        self.assertIn('university'.lower(), response.content.lower())

        response = self.client.get(reverse('kids_about'))
        self.assertIn('kidz'.lower(), response.content.lower())

    def test_win_quest_redirect(self):
        u = add_user('test', 'test@adventurequest.com')
        q = add_quest('city_centre_quest')
        r = add_riddle()
        u = add_user('test', 'test@adventurequest.com')
        # log input
        self.client.post(reverse('login'), {'username':'test', 'password':'123456'})
        response = self.client.post(reverse('city_centre_quest'), {'answer': 'test'})

        self.assertJSONEqual(response.content,{'answer': 'test'})
        self.assertIn('Congratulations'.lower(), response.content.lower())

        #self.assertRedirects(response, '../congratulations/')

    #def test_hall_of_fame(self):
       # add_user('test', 'test@adventureQuest.com', 'testing123')



