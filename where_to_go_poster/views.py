from django.shortcuts import render
from django.views.generic.base import TemplateView

class MainPage(TemplateView):
    template_name = "where_to_go_poster\index.html"



