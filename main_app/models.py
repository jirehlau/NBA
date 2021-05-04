from django.db import models
from django.urls import reverse

class Players(models.Model):
    Name= models.TextField(max_length=200)
    Points= models.IntegerField()
    Rebounds = models.IntegerField()
    Assists = models.IntegerField()
    Steals = models.IntegerField()

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('detail', playersName={'nba_id': self.id})