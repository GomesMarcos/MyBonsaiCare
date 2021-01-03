from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from ..maintenances.models import Maintenance


class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cientific_name = models.CharField(max_length=255, null=True, blank=True)
    maintenances = models.ManyToManyField(Maintenance, verbose_name="Maintenances")
    observations = models.CharField(max_length=1000, null=True, blank=True, default='')
    is_alive = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Plant"
        verbose_name_plural = "Plants"

    def __str__(self):
        return self.name

def get_image_filename(instance, filename):
    title = instance.plant.name
    slug = slugify(title)
    return "media/plant_images/%s-%s" % (slug, filename)

    # def get_absolute_url(self):
    #     return reverse("plant_detail", kwargs={"pk": self.pk})


class PlantPhoto(models.Model):
    plant = models.ForeignKey(Plant, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,verbose_name='Photos')

    class Meta:
        verbose_name = "Plant's photo"
        verbose_name_plural = "Plant's photos"

    # def get_absolute_url(self):
    #     return reverse("plantphoto_detail", kwargs={"pk": self.pk})
