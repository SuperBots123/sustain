from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', include('users.urls', namespace='users')),
    path('feed/', include('feed.urls', namespace='feed')),
    path('challenges/', include('challenges.urls', namespace='challenges')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('friends/', include('friends.urls', namespace='friends')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

