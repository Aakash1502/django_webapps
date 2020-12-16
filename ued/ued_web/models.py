from django.db import models

# Create your models here.
class uxwork(models.Model):
    ux_id = models.AutoField
    ux_name = models.CharField(max_length=50)
    ux_description = models.CharField(max_length=400)
    ux_image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.ux_name

class artwork(models.Model):
    art_id = models.AutoField
    art_name = models.CharField(max_length=50)
    art_description = models.CharField(max_length=400)
    art_image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.art_name