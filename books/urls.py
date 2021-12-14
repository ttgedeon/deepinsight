from django.urls import path
from . import views
app_name = 'books'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('authors/', views.AurhorsView.as_view(), name='authors')
]
