from django.shortcuts import render, HttpResponse
from . import models
#import requests
#import json


def index(request):
    return render(request, 'movies/index.html', {})


def year(request, y):
    movies = models.Movie.objects.filter(release_date__year=y)
    return render(request, 'movies/year.html', {'year': y, 'movies': movies})


def ratings(request):
    """Get list of films order by rating
    """
    movies = models.Movie.objects.all().order_by('-rating', 'name')
    return render(request, 'movies/ratings.html', {'movies': movies})


def detail(request, mid):
    m = models.Movie.objects.get(id=mid)
    #aa = models.Performer.objects.filter()
    return render(request, 'movies/detail.html', {'movie': m})
