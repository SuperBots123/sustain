from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'feed'
urlpatterns = [
    path('', views.FeedView.as_view(), name='feed'),
    path('follow/<int:pk>', views.FollowView.as_view(), name='follow')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)