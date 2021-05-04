from django.shortcuts import render
from . import views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Players

class PlayersCreate(CreateView):
  model = Players
  fields = '__all__'

class PlayersUpdate(UpdateView):
  model = Players
  fields = ['Name', 'Points', 'Rebounds']

class PlayersDelete(DeleteView):
  model = Players
  success_url = '/nba/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def nba_index(request):
  nba = Players.objects.all()
  return render(request, '/index.html', { 'nba': nba })

def nba_detail(request, nba_id):
  nba = Players.objects.get(id=nba_id)
  return render(request, 'nba/detail.html', { 'nba': nba })