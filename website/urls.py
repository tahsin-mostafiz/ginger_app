from django.conf.urls import patterns, url, include
from website import views

urlpatterns = patterns('',
  url(r'^foodtrucks/$', views.foodtrucks, name='truck_list'),
  )
