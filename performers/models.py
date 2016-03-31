from __future__ import unicode_literals

from django.db import models


class Performer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, default='m')
    rating = models.IntegerField(default=0)
    image = models.ImageField(blank=True, null=True)
    musical = models.BooleanField(default=False)

    def _get_full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
    full_name = property(_get_full_name)

    def __unicode__(self):
        return self.full_name
