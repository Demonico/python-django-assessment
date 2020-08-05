# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import RegexValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from statistics import mean


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255, unique=True)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    # Todo: add Rating models

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.pk})

    def rating(self):
        ratings_list = self.ratings.filter(movie_id=self.id)
        if len(ratings_list) > 0:
            return mean(ratings_list.values_list('rating', flat=True))
        else:
            return 'No Ratings'


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="ratings")
    rating = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])
    comments = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.movie_id})
