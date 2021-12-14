from django.shortcuts import render

# Create your views here.
from django.views.generic import (TemplateView, ListView)


class HomeView(TemplateView):
    template_name = 'books/home.html'
