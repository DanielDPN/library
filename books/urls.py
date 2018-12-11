from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new', views.book_new, name='book_new'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('locations', views.location_list, name='location_list'),
    path('location/<int:pk>/', views.location_detail, name='location_detail'),
    path('location/new', views.location_new, name='location_new'),
    path('location/<int:pk>/edit/', views.location_edit, name='location_edit')
]
