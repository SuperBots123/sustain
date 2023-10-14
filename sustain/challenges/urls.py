from django.urls import path

from . import views

app_name = 'challenges'
urlpatterns = [
    path('', views.ChallengeView.as_view(), name='challenges'),
    path('complete_challenge/<int:pk>', views.ChallengeCompleteView.as_view(), name='complete_challenges'),
    path('delete_challenge/<int:pk>', views.ChallengeDeleteView.as_view(), name='delete_challenges'),
]
