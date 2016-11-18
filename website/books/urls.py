from django.conf.urls import *
from books import views

urlpatterns = patterns('',
#        (r'^show/$',views.show),
#        (r'^foo/$',views.foobar_view),
#         (r'^bar/$',views.foobar_view),
         (r'view/$',views.view),
        )

