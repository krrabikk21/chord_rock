from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('theory', views.theory),
    path('chords', views.chords),
    path('pentatonix', views.pentatonix),
    path('metronome', views.metronome),
]
