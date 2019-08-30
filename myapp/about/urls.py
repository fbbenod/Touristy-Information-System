from django.urls import path
from django.views.generic import ListView
from .models import AboutUs,Team
from . import views

urlpatterns = [
    path('', views.about, name='About'),

]

