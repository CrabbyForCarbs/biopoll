# polls/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # The main page: /polls/
    path('', views.index, name='index'),
    # The action for voting: /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]