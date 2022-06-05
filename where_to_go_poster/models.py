from pyexpat import model
from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(max_length=500,verbose_name="название")
    description_short = models.CharField(max_length=1000,verbose_name="короткое описание")
    description_long = HTMLField(verbose_name="длинное описание")
    coordinates = models.TextField(verbose_name="координаты")
    place_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural="places"
        verbose_name = "place"
        db_table = "Places"
        ordering = ('place_order',)
    

    def __str__(self) -> str:
        return self.title


class ImagesPlaces(models.Model):
    place = models.ForeignKey(Places,on_delete=models.CASCADE,verbose_name="место")
    img = models.FileField(upload_to='places/',blank=True,null=True,verbose_name=("изображение"))
    img_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural="images"
        verbose_name = "image"
        db_table = "ImagesPlaces"
        ordering = ('img_order',)
    

    def __str__(self) -> str:
        return f'{self.id} {self.place}'