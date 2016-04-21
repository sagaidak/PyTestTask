from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<article_id>[0-9]+)/$', views.article_page, name='article'),
]


