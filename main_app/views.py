from django.shortcuts import render,redirect
from .models import Game
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TimeForm

# Create your views here.
# Add the following import
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


# def games_index(request):
#     games = Game.objects.all()
#     return render(request, "games/index.html", {"games": games})
class GameList(ListView):
    model = Game
    template_name = "games/index.html"


class GameCreate(CreateView):
    model = Game
    fields = "__all__"
    success_url = "/games/"


class GameUpdate(UpdateView):
    model = Game
    fields = ["genre", "description", "year"]


class GameDelete(DeleteView):
    model = Game
    success_url = "/games/"


def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    time_form = TimeForm()
    return render(request, "games/detail.html", {"game": game, "time_form": time_form})


def add_time(request, game_id):
    form = TimeForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_time = form.save(commit=False)
        new_time.game_id = game_id
        new_time.save()
    return redirect("detail", game_id=game_id)
