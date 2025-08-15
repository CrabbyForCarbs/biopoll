# instabio/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # This puts the poll app under the /polls/ path
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]