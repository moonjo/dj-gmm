from __future__ import unicode_literals

from django.db import models
from performers.models import Performer


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'


class Studio(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(blank=True)
    rating = models.FloatField(default=0)
    duration = models.DurationField(null=True)
    image = models.ImageField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    performers = models.ManyToManyField(Performer, blank=True)
    country = models.ForeignKey(Country, default=1)
    studio = models.ForeignKey(Studio, default=1)
    owned = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, self.release_date)

