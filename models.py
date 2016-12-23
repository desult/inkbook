from django.db import models
from django.core.validators import MaxValueValidator


class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    specs_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

'''
class Series_480_Manager(models.Manager):
    def get_queryset(self):
        return super(Series_480_Manager, self).get_queryset().filter(series="480")
'''


class InkColor(models.Model):
    name = models.CharField(max_length=30)
    pantone = models.CharField(max_length=10, blank=True)
    rgb = models.CharField(max_length=7)
    series = models.ForeignKey(Series, related_name="color_of_series")
#    objects = models.Manager()
#    objects_480 = Series_480_Manager()

    def __str__(self):
        return self.name
