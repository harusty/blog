#coding=utf-8

from django.conf.urls import url

from post import views

urlpatterns=[
    url(r'^$',views.queryAll),
    url(r'^page/(\d+)$',views.queryAll)
]