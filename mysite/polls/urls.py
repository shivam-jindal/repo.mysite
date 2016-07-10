from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^questions/$', views.questions, name='questions'),
	url(r'^selectquestion/$', views.selectquestion, name='selectquestion'),
	url(r'^editprofile/$', views.editprofile, name='editprofile'),
	url(r'^changepassword/$', views.changepassword, name='changepassword'),
)
