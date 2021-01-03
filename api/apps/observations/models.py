from django.db import models

from ..plants.models import Plant


class Observation(models.Model):
  plant_name = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    pass

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Observation'