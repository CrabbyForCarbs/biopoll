# instabio/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # This now correctly points the homepage to your polls app
    path('', include('polls.urls')),
    
    path('admin/', admin.site.urls),
]