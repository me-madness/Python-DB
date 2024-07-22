from django.db import models


class ProfileManager(models.Manager):
    def get_regular_customers():
        