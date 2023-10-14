from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.ProfileView.as_view(), name="profile"),
]
