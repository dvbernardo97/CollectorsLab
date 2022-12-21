from django.shortcuts import render, redirect
from .models import Game, Content
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TimeForm

# Create your views here.
# Add the following import
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


class GameList(ListView):
    model = Game
    template_name = "games/index.html"


class GameCreate(CreateView):
    model = Game
    fields = ["name", "genre", "description", "year"]
    success_url = "/games/"


class GameUpdate(UpdateView):
    model = Game
    fields = ["genre", "description", "year"]


class GameDelete(DeleteView):
    model = Game
    success_url = "/games/"


def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    id_list = game.contents.all().values_list("id")
    content_not_included = Content.objects.exclude(id__in=id_list)
    time_form = TimeForm()
    return render(
        request,
        "games/detail.html",
        {"game": game, "time_form": time_form, "contents": content_not_included},
    )


def add_time(request, game_id):
    form = TimeForm(request.POST)
    # validate the form
    if form.is_valid():
        new_time = form.save(commit=False)
        new_time.game_id = game_id
        new_time.save()
    return redirect("detail", game_id=game_id)


class ContentList(ListView):
    model = Content


class ContentDetail(DetailView):
    model = Content


class ContentCreate(CreateView):
    model = Content
    fields = "__all__"


class ContentUpdate(UpdateView):
    model = Content
    fields = ["name", "color"]


class ContentDelete(DeleteView):
    model = Content
    success_url = "/contents/"


def ext_contents(request, game_id, contents_id):
    Game.objects.get(id=game_id).contents.add(contents_id)
    return redirect("detail", game_id=game_id)
