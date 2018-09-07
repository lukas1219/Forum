from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self): #Definiujemy funkcje, która zwraca tytuł wpisu
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self): #Definiujemy funkcje, która zwraca tytuł wpisu
        return self.title
