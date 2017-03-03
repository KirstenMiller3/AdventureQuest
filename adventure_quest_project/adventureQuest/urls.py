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
	url(r'^quest1riddle1/$', views.answer_riddle, name='quest1riddle1'),
]
