from django.urls import path

from . import views

app_name = 'challenges'
urlpatterns = [
    path('', views.ChallengeView.as_view(), name='challenges'),
]
