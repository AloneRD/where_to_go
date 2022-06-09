import os
from urllib.parse import urlparse
from io import BytesIO
import requests
from django.core.management.base import BaseCommand
from where_to_go_poster.models import Places
from where_to_go_poster.models import ImagesPlaces


class Command(BaseCommand):
    help = 'Add places in DataBase'

    def add_arguments(self, parser):
        parser.add_argument('link', nargs='+', type=str, help='Link to JSON')

    def handle(self, *args, **options):
        requests_data_place = requests.get(fr"{options['link'][0]}")
        requests_data_place.raise_for_status()
        data_place = requests_data_place.json()
        if 'error' in data_place:
            raise requests.exceptions.HTTPError(data_place['error'])
        place, created = Places.objects.get_or_create(
            title=data_place['title'],
            coordinates=data_place['coordinates'],
            defaults={
                'description_short': data_place['description_short'],
                'description_long': data_place['description_long']
                }
        )
        images = []
        for img in data_place['imgs']:
            name = os.path.splitext(os.path.split(urlparse(img).path)[1])[0]
            content_request = requests.get(img)
            content_request.raise_for_status()         
            content = content_request.content
            images.append(
                {
                    "content": BytesIO(content),
                    "name": name
                }
                )

        for image in images:
            new_place = ImagesPlaces(place=place)
            new_place.img.save(
                f"{image['name']}.img",
                image['content'], save=True
                )
