from django.urls import path
from .views import home, about, detail


urlpatterns = [
    path('', home, name='home'),
    path('product/<str:slug>', detail, name='detail'),
    path('about/', about, name='about'),
]