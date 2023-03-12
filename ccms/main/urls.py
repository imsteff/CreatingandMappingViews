from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mission/", views.mission, name="mission"),
    path("vision/", views.vision, name="mission"),
    path("objectives/", views.objectives, name="mission"),
]
