from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    
    path('', include('users.urls', namespace='users')),
    path('feed/', include('feed.urls', namespace='feed')),
    path('challenges/', include('challenges.urls', namespace='challenges')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
