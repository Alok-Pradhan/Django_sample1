from typing import ValuesView
from django.contrib import admin
#admin.autodiscover()
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('login/' , views.login, name='login'),
    path('signup/', views.signupa, name = 'signup'),
    path('auth/', views.auth, name = 'auth'),
    path('mail/', views.mail, name = 'mail'),
    path('sms/', views.sms_send, name = 'sms'),
    #path('admin/', admin.site.urls, name='admin')

]