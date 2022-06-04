from django.contrib import admin
from where_to_go_poster.models import Places
from where_to_go_poster.models import ImagesPlaces

class ImagePlaceInline(admin.TabularInline):
    model = ImagesPlaces

@admin.register(Places)
class AdminPlace(admin.ModelAdmin):
    inlines = [ImagePlaceInline]

admin.site.register(ImagesPlaces)