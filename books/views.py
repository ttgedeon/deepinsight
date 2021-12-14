from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, CreateView, DetailView)
from . import models


class HomeView(TemplateView):
    template_name = 'books/home.html'


class AuthorListview(ListView):
    template_name = 'books/author_list.html'
    queryset = models.Author.objects.all()
    context_object_name = 'authors_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        return super(AuthorListview, self).get_context_data(**kwargs)


class AuthorCreateView(CreateView):
    template_name = 'books/author_create.html'
    queryset = models.Author.objects.all()
    fields = '__all__'

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The author has been created successfully'
        )
        return super(AuthorCreateView, self).form_valid(form)


class AuthorDetailView(DetailView):
    model = models.Author
    template_name = 'books/author_detail.html'
