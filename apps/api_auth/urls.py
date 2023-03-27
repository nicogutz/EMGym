from django.urls import path
from . import views

urlpatterns = [
    path("core/device/<int:uid>", views.DeviceView.as_view(), name="device"),
    path("core/exercise/", views.ExerciseCreate().as_view(), name="exercise_create"),
    path("core/datum/", views.DatumCreate().as_view(), name="data_create"),
]
