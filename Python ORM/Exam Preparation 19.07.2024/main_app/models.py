from django.db import models

# Create your models here.

class DirectorModel(models.Model):
    name = models.CharField(
        max_length=100
    )


class ActorModel(models.Model):
    name = models.CharField(
        max_length=100
    )


class MovieModel(models.Model):
    name = models.CharField(
        max_length=100
    )