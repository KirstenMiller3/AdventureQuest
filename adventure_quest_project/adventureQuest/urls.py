from django.conf.urls import url
from adventureQuest import views

urlpatterns = [
	#Remeber commas
	url(r'^$', views.index, name='index'),
	# url(r'^about/$', views.about, name='about'),
	# url(r'^add_category/$', views.add_category, name='add_category'),
	# url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
	# url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
	url(r'^register/$',views.register,name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	# url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^quest1_about/$', views.quest1_about, name='quest1_about'),
	url(r'^finnieston_about/$', views.finnieston_about, name='finnieston_about'),
	#url(r'^test_quest/$', views.answer_riddle, name='test_quest'),
	url(r'^glasgow_uni_about/$', views.glasgow_uni_about, name='glasgow_uni_about'),
	url(r'^southside_about/$', views.southside_about, name='southside_about'),
	url(r'^city_centre_about/$', views.city_centre_about, name='city_centre_about'),
	url(r'^kids_about/$', views.kids_about, name='kids_about'),
	url(r'^congratulations/$', views.congratulations, name='congratulations'),

	url(r'^test_quest/$', views.test_quest, name='test_quest'),
	url(r'^finnieston_quest/$', views.finnieston_quest, name='finnieston_quest'),
	url(r'^glasgow_uni_quest/$', views.glasgow_uni_quest, name='glasgow_uni_quest'),
	url(r'^southside_quest/$', views.southside_quest, name='southside_quest'),
	url(r'^city_centre_quest/$', views.city_centre_quest, name='city_centre_quest'),
	url(r'^kids_quest/$', views.kids_quest, name='kids_quest'),

	url(r'^quest_ajax/$', views.quest_ajax, name='quest_ajax'),
	url(r'^my_account/$', views.my_account, name='my_account'),
	url(r'^post_list/$', views.post_list, name='post_list'),
	url(r'^post_form/$', views.post_create, name='post_form'),
	url(r'^hall_of_fame/$', views.hall_of_fame, name='hall_of_fame'),

]
