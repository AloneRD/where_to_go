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
        get_place_response = requests.get(fr"{options['link'][0]}")
        get_place_response.raise_for_status()
        place = get_place_response.json()
        if 'error' in place:
            raise requests.exceptions.HTTPError(place['error'])
        place_coordinates = dict(place["coordinates"])
        place, created = Places.objects.get_or_create(
            title=place['title'],
            coordinate_lng=place_coordinates["lng"],
            coordinate_lat=place_coordinates["lat"],
            defaults={
                'description_short': place['description_short'],
                'description_long': place['description_long']
                }
        )
        images = []
        for img in place['imgs']:
            name = os.path.splitext(os.path.split(urlparse(img).path)[1])[0]
            content_request = requests.get(img)
            content_request.raise_for_status()
            content = content_request.content
            images.append({
                    "content": BytesIO(content),
                    "name": name
                    })

        for image in images:
            new_place = ImagesPlaces(place=place)
            new_place.img.save(
                f"{image['name']}.img",
                image['content'], save=True
                )
