from django.db import models
from django.urls import reverse

VIDEOS = (("M", "Morning"), ("A", "Afternoon"), ("E", "Evening"))

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"game_id": self.id})


class Time(models.Model):
    date = models.DateField("Game Time")
    gaming = models.CharField(max_length=1, choices=VIDEOS, default=VIDEOS[0][0])

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_gaming_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]
