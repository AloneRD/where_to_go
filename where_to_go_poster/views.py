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
        places = Places.objects.all()
        features = []
        for place in places:
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.coordinate_lng, place.coordinate_lat]
                    },
                "properties": {
                    "title": place.title,
                    "placeId": f"{place.id}",
                    "detailsUrl": reverse('places_detail', kwargs={"pk": place.id})
                }
            }
            features.append(feature)
        places_for_site = {
            "type": "FeatureCollection",
            "features": features
        }
        context['places'] = places_for_site
        return context


class PlacesDetail(DetailView):
    model = Places

    def get(self, request, *args, **kwargs) -> JsonResponse:
        self.object = self.get_object()
        images = [image.img.url for image in ImagesPlaces.objects.filter(place_id=self.object.id)]
        place = {
            "title": self.object.title,
            "imgs": images,
            "description_short": self.object.description_short,
            "description_long": self.object.description_long,
            "coordinates": {
                "lat": self.object.coordinate_lat,
                "lng": self.object.coordinate_lng
                }
        }
        return JsonResponse(place, safe=False, json_dumps_params={'ensure_ascii': False})
