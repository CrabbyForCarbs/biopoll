# polls/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # The main page: /polls/
    path('', views.homepage, name='homepage'),
    # The action for voting: /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]