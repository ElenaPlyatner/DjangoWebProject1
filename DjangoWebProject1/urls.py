"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.forms
import app.views
from django.shortcuts import render, redirect
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Авторизация',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^anketa$', app.views.anketa, name='anketa'),
    url(r'^newpost$', app.views.newpost, name='newpost'),
    url(r'^registration$', app.views.registration, name='registration'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^catalog$', app.views.catalog, name='catalog'),
    url(r'^trash$', app.views.trash, name='trash'),
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
    url(r'^addtotrash/(?P<aid>\d+)/$', app.views.addtotrash, name='addtotrash'),
    url(r'^delproduct/(?P<did>\d+)/$', app.views.delproduct, name='delproduct'),
    url(r'^buyproduct/(?P<bid>\d+)/$', app.views.buyproduct, name='buyproduct'),
    url(r'^videopost$', app.views.videopost, name='videopost'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
