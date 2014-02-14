from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gingerfoodapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^gingerapp/', include('website.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
