"""
Definition of urls for Chatty.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import views as appViews, forms as appForms
import app

urlpatterns = [
    path('', appViews.home, name='home'),
    path('join-global-chat/', appViews.globalchatlanding, name='globalchatlanding'),
    path('global-chat/', appViews.globalchat, name='globalchat'),
    path('one-on-one-chat/', appViews.oneonone, name='oneonone'),
    path('login/', appViews.loginView, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
