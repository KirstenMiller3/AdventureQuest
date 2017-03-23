from django.conf.urls import url
from adventureQuest import views

############################################
#   This is the urls for Adventure Quest   #
############################################

urlpatterns = [

	# Home Page
	url(r'^$', views.index, name='index'),

	# Hall of Fame
	url(r'^hall_of_fame/$', views.hall_of_fame, name='hall_of_fame'),

	# Congratulations page for when you complete a quest.
	url(r'^congratulations/$', views.congratulations, name='congratulations'),

	# URL's for posting a Hall of Fame Post and for making and displaying comments.
	url(r'^post_form/$', views.post_create, name='post_form'),
	url(r'^comment/$', views.comment, name='comment'),
	url(r'^comment_form/$', views.add_comment, name='add_comment'),

	# URL's to do with user login functionality
	url(r'^register/$',views.register,name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^my_account/$', views.my_account, name='my_account'),

	# URL's for the quest about pages.
	url(r'^mystery_about/$', views.mystery_about, name='mystery_about'),
	url(r'^finnieston_about/$', views.finnieston_about, name='finnieston_about'),
	url(r'^glasgow_uni_about/$', views.glasgow_uni_about, name='glasgow_uni_about'),
	url(r'^southside_about/$', views.southside_about, name='southside_about'),
	url(r'^city_centre_about/$', views.city_centre_about, name='city_centre_about'),
	url(r'^kids_about/$', views.kids_about, name='kids_about'),

	# URL's for the quest riddle pages.
	url(r'^mystery_quest/$', views.mystery_quest, name='mystery_quest'),
	url(r'^finnieston_quest/$', views.finnieston_quest, name='finnieston_quest'),
	url(r'^glasgow_uni_quest/$', views.glasgow_uni_quest, name='glasgow_uni_quest'),
	url(r'^southside_quest/$', views.southside_quest, name='southside_quest'),
	url(r'^city_centre_quest/$', views.city_centre_quest, name='city_centre_quest'),
	url(r'^kids_quest/$', views.kids_quest, name='kids_quest'),

	# URL's for the quest hall of fame pages.
	url(r'^mystery_quest_hall_of_fame/$', views.mystery_quest_hall_of_fame, name='mystery_quest_hall_of_fame'),
	url(r'^finnieston_quest_hall_of_fame/$', views.finnieston_quest_hall_of_fame, name='finnieston_quest_hall_of_fame'),
	url(r'^glasgow_uni_quest_hall_of_fame/$', views.glasgow_uni_quest_hall_of_fame, name='glasgow_uni_quest_hall_of_fame'),
	url(r'^southside_quest_hall_of_fame/$', views.southside_quest_hall_of_fame, name='southside_quest_hall_of_fame'),
	url(r'^city_centre_quest_hall_of_fame/$', views.city_centre_quest_hall_of_fame, name='city_centre_quest_hall_of_fame'),
	url(r'^kids_quest_hall_of_fame/$', views.kids_quest_hall_of_fame, name='kids_quest_hall_of_fame'),

	# URL for ajax functionality to handle riddle logic.
	url(r'^quest_ajax/$', views.quest_ajax, name='quest_ajax'),

]
