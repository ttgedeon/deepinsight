from django.urls import path
from . import views
app_name = 'books'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authors/', views.AuthorListview.as_view(), name='authors'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='add_author'),
    path('aurhors/<uuid:pk>/', views.AuthorDetailView.as_view(), name='author_detail')
]
