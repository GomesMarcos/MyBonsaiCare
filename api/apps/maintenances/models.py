from django.db import models



class Maintenance(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True, blank=True)
    schedule = models.DateTimeField()

    class Meta:
        verbose_name = "Maintenance"
        verbose_name_plural = "Maintenances"

    def __str__(self):
        return self.name
