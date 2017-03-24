####  THIS IS THE URLS FOR CAPSTONE LID
from django.conf.urls import url

from . import views
app_name='aum'
urlpatterns = [
    # ex: /aum/
    url(r'^$', views.index, name='index'),
    # ex: /aum/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /aum/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /aum/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #trying something new here with USER
    # ex:/aum/2/user
    url(r'^(?P<user_id>[0-9]+)/user/$', views.user, name = 'user'),
    #make a new user view that shows true if the user exists with the correct password and false otherwise
    #url(r'^(?P<u>[0-9a-zA-Z]+)/(?P<p>[0-9a-zA-Z]+)/login/$', views.login, name = 'login'),
    #trying somthing new here where we just use /login and a POST type request
    url(r'^login/$', views.login, name = 'login'),


]