from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,

)
from . import views

urlpatterns=[
    path('', PostListView.as_view(), name='Hotels'),
    path('<int:pk>/', PostDetailView.as_view(), name='Hotel1'),
    path('<int:hotel_id>', views.add_review, name='add_review')
]
