from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.MainPage.as_view(),name='main_page'),
    path('places/<int:pk>',views.PlacesDetail.as_view(),name="places_detail")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
