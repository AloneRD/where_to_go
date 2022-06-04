import re
import json
from django.shortcuts import render
from django.views.generic.base import TemplateView
from where_to_go_poster.models import Places

class MainPage(TemplateView):
    template_name = "where_to_go_poster\index.html"


    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        query_set_places = Places.objects.all()
        features = []
        for place in query_set_places:
            coordinates = eval(place.coordinates)
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [coordinates["lng"], coordinates["lat"]]
                    },
                "properties": {
                "title": f"{re.search(r'«(.*)»',place.title).group(0)}",
                "placeId": f"{place.id}",
                "detailsUrl": f"static/places/{place.id}.json"
                }
            }
            features.append(feature)
        json_places = {
            "type": "FeatureCollection",
            "features": features
        }
        context['json_places'] = json_places
        return context



