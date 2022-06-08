from django.contrib import admin
from where_to_go_poster.models import Places
from where_to_go_poster.models import ImagesPlaces
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from adminsortable2.admin import SortableAdminMixin


class ImagePlaceInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ImagesPlaces
    extra = 2
    readonly_fields = ("img_show",)

    def img_show(self, instance):
        return format_html('<img src="{}" width=200px  height=220px style="object-fit:contain"> ', instance.img.url)


@admin.register(Places)
class AdminPlace(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ImagePlaceInline]


admin.site.register(ImagesPlaces)
