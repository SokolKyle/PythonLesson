from django.db import models


class Skils(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='skils/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

