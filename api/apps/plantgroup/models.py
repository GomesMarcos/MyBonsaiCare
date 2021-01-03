from django.db import models

from ..plants.models import Plant


class PlantGroup(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    plant = models.ForeignKey(Plant, related_name="plant_group", on_delete=models.CASCADE)

    # class Meta:
    #     verbose_name = _("PlantGroup")
    #     verbose_name_plural = _("PlantGroups")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("PlantGroup_detail", kwargs={"pk": self.pk})
