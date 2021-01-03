from django.db import models
from django.contrib.auth.models import User 

from ..plants.models import Plant

class Graveyard(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  plant_name = models.ForeignKey(Plant, on_delete=models.CASCADE)

  def __str__(self):
    pass

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Graveyard'