from django.conf.urls import patterns, url, include
from django.contrib import admin
from website import views

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^foodtrucks/$', views.get_foodtrucks, name='get_truck_list'),
  )

urlpatterns = patterns('',
  url(r'^foodtrucks/update$', views.update_foodtrucks, name='update_truck_list'),
  )
