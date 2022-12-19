from django.shortcuts import render
from django.http import HttpResponse


class Game:
    def __init__(self, name, genre, description, year):
        self.name = name
        self.genre = genre
        self.description = description
        self.year = year


games = [
    Game("Fantasy", "Genshin", "mobile game", 2020),
    Game("FPS", "MW2", "War game", 2022),
    Game("RPG", "Final Fantasy", "Story Game", 1990),
]


# Create your views here.
# Add the following import
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

    # Add new view


def games_index(request):
    return render(request, "games/index.html", {"games": games})
