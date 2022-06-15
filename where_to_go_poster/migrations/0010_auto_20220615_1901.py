# Generated by Django 3.0 on 2022-06-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go_poster', '0009_auto_20220615_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='coordinates',
        ),
        migrations.AddField(
            model_name='places',
            name='coordinate_lat',
            field=models.FloatField(default=0, verbose_name='ширина'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='places',
            name='coordinate_lng',
            field=models.FloatField(default=0.0, verbose_name='долгота'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagesplaces',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='places/', verbose_name='изображение'),
        ),
    ]
