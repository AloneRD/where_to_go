# Generated by Django 3.0 on 2022-06-05 04:57

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('where_to_go_poster', '0006_alter_places_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='длинное описание'),
        ),
    ]