from django.db import models
from common.models import Datation
# Create your models here.


class Author(Datation):

    name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.name


class Book(Datation):
    title = models.CharField(null=False, blank=False, max_length=255)
    author = models.ForeignKey(Author, null=False, blank=False, on_delete=models.PROTECT,
                               related_name='author_books')
