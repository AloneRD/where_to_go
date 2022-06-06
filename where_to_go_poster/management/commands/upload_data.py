from io import BytesIO
import requests
import re
from django.core.management.base import BaseCommand
from where_to_go_poster.models import Places
from where_to_go_poster.models import ImagesPlaces

class Command(BaseCommand):
    help = 'Add places in DataBase'

    def add_arguments(self, parser):
        parser.add_argument('link', nargs='+', type=str,help='Link to data file')

    def handle(self, *args, **options):
        data_place = requests.get(fr"{options['link'][0]}").json()
        place,created = Places.objects.get_or_create(
            title=data_place['title'],
            description_short = data_place['description_short'],
            description_long = data_place['description_long'],
            coordinates =  data_place['coordinates']    
        )
        print(place)
        images = [{"content":BytesIO(requests.get(img).content),"name":re.findall(r"(.*)\/(.*).jpg|JPG|Jpg|jpeg|JPEG", img)[0][1]} for img in data_place['imgs']]
        for image in images:
            new_place = ImagesPlaces(place = place)
            new_place.img.save(f"{image['name']}.img",image['content'],save=True)
