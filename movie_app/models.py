from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=100, null=True, blank=not False)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title
    
    
class Review(models.Model):
    text = models.TextField(max_length=150, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return self.text
