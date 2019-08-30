from django.urls import path
from . import views
from .views import (
    PostDetailView,
    PostListView
)

urlpatterns = [
    path('',  PostListView.as_view(), name='Home'),
    path('home/<int:pk>/', PostDetailView.as_view(), name='index2')
]
