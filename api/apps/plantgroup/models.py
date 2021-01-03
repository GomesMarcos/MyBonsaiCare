from django.db import models

from ..plants.models import Plant


class PlantGroup(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True, default='')
    plants = models.ManyToManyField(Plant, verbose_name="Plents")

    class Meta:
        verbose_name = "Plant Group"
        verbose_name_plural = "Plant Groups"

    def __str__(self):
        return self.name
