from django.forms.models import inlineformset_factory
from .models import Author, Book

AuthorBooksFormset = inlineformset_factory(
    parent_model=Author, model=Book, fields=('title',)
)
