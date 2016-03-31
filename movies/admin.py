from django.contrib import admin
from .models import Genre, Country, Studio, Movie

@admin.register(Genre, Country, Studio, Movie)
class MoviesAdmin(admin.ModelAdmin):
    pass