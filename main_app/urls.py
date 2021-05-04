from django.shortcuts import render
from .models import Players
from django.urls import path
from main_app import views 

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('nba/', views.nba_index, name='index'),
  path('nba/<int:nba_id>/', views.nba_detail, name='detail'),
  path('nba/create/', views.PlayersCreate.as_view(), name='nba_create'),
  path('nba/<int:pk>/update/', views.PlayersUpdate.as_view(), name='nba_update'),
  path('nba/<int:pk>/delete/', views.PlayersDelete.as_view(), name='nba_delete'),
]