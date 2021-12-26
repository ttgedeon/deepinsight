from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
app_name = 'books'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authors/', views.AuthorListview.as_view(), name='authors'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='add_author'),
    path('authors/<uuid:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/<uuid:pk>/books/edit/', views.AuthorBooksEditView.as_view(), name='author_book_edit'),
]
