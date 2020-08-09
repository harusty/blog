# coding=utf-8

from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^$', views.queryAll),
    url(r'^page/(\d+)$', views.queryAll),
    url(r'^post/(\d+)$', views.postDetail),
    url(r'^archive/(\d+)/(\d+)$', views.queryPostByCreated),
    url(r'^category/(\d+)$', views.queryPostByCid),
]
