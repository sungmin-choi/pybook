from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^login/$', views.login),
    url(r'^join/$', views.join),
    url(r'^search/$', views.search),
    url(r'^logout/$', views.logout),
    url(r'^me/$', views.userDetail),
]
