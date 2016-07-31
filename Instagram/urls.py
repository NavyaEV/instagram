from django.conf.urls import url,patterns,include
from Instagram import views
from django.conf.urls import patterns, include, url
from Instagram.views import *

urlpatterns = [
    url(r'add?$',views.create_View.as_view(),name="list"),
    url(r'^$',views.class_View.as_view(),name="imageList"),

    #url(r'^list/$',list,name="list"),
]