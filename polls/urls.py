from django.conf.urls import url

from . import views

app_name='polls'
urlpatterns = [
	# /polls
	url(r'^$', views.IndexView.as_view(), name='index'),
	# /polls/num/
	url(r'^(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# /polls
	url(r'^(?P<question_id>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	# /polls
	url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
]