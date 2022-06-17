from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(max_length=200, verbose_name="название",)
    description_short = models.TextField(blank=True, verbose_name="короткое описание")
    description_long = HTMLField(blank=True, verbose_name="длинное описание")
    coordinate_lng = models.FloatField(verbose_name="долгота")
    coordinate_lat = models.FloatField(verbose_name="ширина")

    class Meta:
        verbose_name_plural = "places"
        verbose_name = "place"
        db_table = "Places"

    def __str__(self) -> str:
        return self.title


class ImagesPlaces(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE, related_name="images", verbose_name="место")
    img = models.ImageField(upload_to='places/', verbose_name="изображение")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "images"
        verbose_name = "image"
        db_table = "ImagesPlaces"
        ordering = ('order',)

    def __str__(self) -> str:
        return f'{self.order} {self.place}'
