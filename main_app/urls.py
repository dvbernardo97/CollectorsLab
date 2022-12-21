from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # path("games/", views.games_index, name="game"),
    path("games/", views.GameList.as_view(), name="game"),
    path("games/<int:game_id>", views.games_detail, name="detail"),
    path("games/<int:pk>/update/", views.GameUpdate.as_view(), name="games_update"),
    path("games/<int:pk>/delete/", views.GameDelete.as_view(), name="games_delete"),
    path("games/create/", views.GameCreate.as_view(), name="games_create"),
    path("games/<int:game_id>/add_time/", views.add_time, name="add_time"),
]
