from django.db import models

class AstronautManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            mission_count=models.Count('mission')
        ).order_by('-mission_count', 'phone_number')

    def get_astronauts_by_missions_count(self):
        return self.get_queryset()