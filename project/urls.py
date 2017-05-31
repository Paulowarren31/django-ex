from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, secret, profile, table
import django_saml2_auth.views


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^saml2_auth/', include('django_saml2_auth.urls')),
    url(r'^accounts/login/$', django_saml2_auth.views.signin),

    url(r'^$', index),
    url(r'^table/', table),
    url(r'^secret$', secret),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ht/$', include('health_check.urls')),

]
