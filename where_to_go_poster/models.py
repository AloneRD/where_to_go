from pyexpat import model
from django.db import models
from django.forms import model_to_dict


class Places(models.Model):
    title = models.CharField(max_length=500,verbose_name="название")
    description_short = models.CharField(max_length=1000,verbose_name="короткое описание")
    description_long = models.TextField(verbose_name="длинное описание")
    coordinates = models.TextField(verbose_name="координаты")

    class Meta:
        verbose_name_plural="places"
        verbose_name = "place"
        db_table = "Plaases"
    

    def __str__(self) -> str:
        return self.title