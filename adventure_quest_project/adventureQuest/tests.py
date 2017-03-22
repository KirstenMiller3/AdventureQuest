from django.test import TestCase
from adventureQuest.models import Post, UserProfile
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your tests here.
def add_user(username, email, password):
    u = UserProfile.create(username=username)
    u.email = email
    u.user.set_password(password)
    u.save()
    return u


def add_post(user, quest, title, image, )

class AdventureQuestTests(TestCase):


    def test_add_post_something(self):
        """
        fsdg
        """
        u = add_user('test', 'test@adventurequest.com','123456')
        p = Post(user=u, quest='mystery_quest', title = 'Test', image='', content='Testing' )
        p.save()
        self.assertEqual(response.status_code, 200)

    def test_pages_while_logged_out(self):
        gfs



    def test_pages_while_logged_in(self):
        ssgr

    def test_hall_of_fame(self):
        add_user('test', 'test@adventureQuest.com', 'testing123')



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
    hints = models.IntegerField(default=-1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
        #return reverse('post_create', kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]


