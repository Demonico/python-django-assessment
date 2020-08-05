# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', view=views.MovieListView.as_view(), name='index'),
    path('create_rating/', view=views.RatingCreateView.as_view(), name='rate'),
    path('<int:id>/ratings/', view=views.RatingListView.as_view(), name='ratings'),
    path('<int:id>/', view=views.MovieDetailView.as_view(), name='detail'),
    path('create/', view=views.MovieCreateView.as_view(), name='create'),
    path('update/<int:id>/', view=views.MovieUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', view=views.MovieDeleteView.as_view(), name='delete'),
]
