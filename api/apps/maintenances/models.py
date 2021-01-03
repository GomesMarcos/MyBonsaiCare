from django.db import models

from ..plants.models import Plant


class Maintenance(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    plant_name = models.ManyToManyField(Plant)
    schedule = models.DateTimeField()

    # class Meta:
    #     verbose_name = _("maintenance")
    #     verbose_name_plural = _("maintenances")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("maintenance_detail", kwargs={"pk": self.pk})
