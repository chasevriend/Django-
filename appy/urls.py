from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("chase", views.chase, name="chase"),
    path("daniel", views.daniel, name="daniel")
]