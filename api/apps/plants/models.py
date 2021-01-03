from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cientific_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "plant"
        verbose_name_plural = "plants"

    def __str__(self):
        return self.name

def get_image_filename(instance, filename):
    title = instance.plant.name
    slug = slugify(title)
    return "plant_images/%s-%s" % (slug, filename)

    # def get_absolute_url(self):
    #     return reverse("plant_detail", kwargs={"pk": self.pk})


class PlantPhoto(models.Model):
    plant = models.ForeignKey(Plant, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,verbose_name='Photos')

    class Meta:
        verbose_name = "plantphoto"
        verbose_name_plural = "plantphotos"

    # def get_absolute_url(self):
    #     return reverse("plantphoto_detail", kwargs={"pk": self.pk})
