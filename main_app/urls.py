from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("games/", views.GameList.as_view(), name="game"),
    path("games/<int:game_id>", views.games_detail, name="detail"),
    path("games/<int:pk>/update/", views.GameUpdate.as_view(), name="games_update"),
    path("games/<int:pk>/delete/", views.GameDelete.as_view(), name="games_delete"),
    path("games/create/", views.GameCreate.as_view(), name="games_create"),
    path("games/<int:game_id>/add_time/", views.add_time, name="add_time"),
    path(
        "games/<int:game_id>/ext_contents/<int:contents_id>/",
        views.ext_contents,
        name="ext_contents",
    ),
    path("contents/", views.ContentList.as_view(), name="contents_index"),
    path("contents/<int:pk>/", views.ContentDetail.as_view(), name="contents_detail"),
    path("contents/create/", views.ContentCreate.as_view(), name="contents_create"),
    path(
        "contents/<int:pk>/update/",
        views.ContentUpdate.as_view(),
        name="content_update",
    ),
    path(
        "contents/<int:pk>/delete/",
        views.ContentDelete.as_view(),
        name="content_delete",
    ),
]
