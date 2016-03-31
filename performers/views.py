from django.shortcuts import render, HttpResponse
from . import models

def index(request):
    all_performers = models.Performer.objects.all()
    return render(request, 'performer/index.html', {'performers': all_performers})


def detail(request, pid):
    performer = models.Performer.objects.get(id=pid)
    if performer:
        movies = models.Movie.objects.filter(actors__in=[performer])
    else:
        movies = []
    all_performers = models.Performer.objects.all()
    return render(request, 'movies/actor.html',
                  {'actor': performer, 'performers': all_performers, 'movies': movies}
                  )
