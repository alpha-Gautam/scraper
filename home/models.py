from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.TextField()  # Store as comma-separated values
    plot = models.TextField()
    poster_url = models.URLField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField()
    external_url = models.URLField()

    def __str__(self):
        return self.title
    
    
