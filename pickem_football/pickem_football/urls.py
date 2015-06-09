from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pickem_football.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pickem/$', include('game.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
