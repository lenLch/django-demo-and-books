#coding=utf-8
"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
#import website.views
from django.conf import settings

urlpatterns = patterns('website.views',
    url(r'^admin/', admin.site.urls),
    (r'^$','my_homepage_view'),
    (r'^hello/$','hello'),
    (r'^time/$','current_datetime'),    
    (r'^time/plus/(?P<offset>\d{1,2})/$','hour_ahead'),
    (r'xiaomi/$','xiaomi'),
    (r'name/$','name'),
    (r'meta/$','display_meta'),
    )

urlpatterns = patterns('',
        (r'^books/',include('books.urls')),
        
        )

urlpatterns += patterns('books.views',
#           url(r'^show/','show'), 
           url(r'search-form/$','search_form'),
#           url(r'search/$','search'),
           url(r'search/$','search1'),
#           url(r'^foo/$','foobar_view',{'template_name':'template1.html'}),
#           url(r'^bar/$','foobar_view',{'template_name':'template2.html'}),
            
        )

urlpatterns += patterns('contact.views',
            url(r'^contact/$','contact1'),
            url(r'contact/thanks/$','thanks'),
        )

if settings.DEBUG:
    urlpatterns += patterns('',
#            (r'^debuginfo/$',website.views.debug),
            )
