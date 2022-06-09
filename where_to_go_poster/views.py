from django.http import JsonResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from where_to_go_poster.models import Places
from where_to_go_poster.models import ImagesPlaces


class MainPage(TemplateView):
    template_name = "where_to_go_poster\\index.html"

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
                    "title": place.title,
                    "placeId": f"{place.id}",
                    "detailsUrl": reverse('places_detail', kwargs={"pk": place.id})
                }
            }
            features.append(feature)
        json_places = {
            "type": "FeatureCollection",
            "features": features
        }
        context['json_places'] = json_places
        return context


class PlacesDetail(DetailView):
    model = Places

    def get(self, request, *args, **kwargs) -> JsonResponse:
        self.object = self.get_object()
        images = [image.img.url for image in ImagesPlaces.objects.filter(place_id=self.object.id)]
        json_place = {
            "title": self.object.title,
            "imgs": images,
            "description_short": self.object.description_short,
            "description_long": self.object.description_long,
            "coordinates": self.object.coordinates
        }
        return JsonResponse(json_place, safe=False, json_dumps_params={'ensure_ascii': False})
