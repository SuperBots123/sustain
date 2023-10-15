from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'challenges'
urlpatterns = [
    path('', views.ChallengeView.as_view(), name='challenges'),
    path('delete_challenge/<int:pk>', views.ChallengeDeleteView.as_view(), name='delete_challenges'),
]
