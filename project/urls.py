from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, secret, profile

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^secret$', secret),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('djangosaml2.urls')),
    url(r'^accounts/profile', profile),
]
