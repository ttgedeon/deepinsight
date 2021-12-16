from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.views.generic.detail import SingleObjectMixin
from . import models
from .forms import AuthorBooksFormset


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


class AuthorBooksEditView(SingleObjectMixin, FormView):

    model = models.Author
    template_name = 'books/author_books_edit.html'
    form_class = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Author.objects.all())
        return super(AuthorBooksEditView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Author.objects.all())
        return super(AuthorBooksEditView, self).post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return AuthorBooksFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Changes save successfully")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('books:author_detail', kwargs={"pk": self.object.pk})
