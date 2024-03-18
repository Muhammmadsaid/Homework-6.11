from django.urls import path
from . import views

urlpatterns = [
   path('', views.theme_list, name='theme_list'),
   path('add/', views.add_theme, name='add_theme'),
   path('edit/<int:pk>/', views.edit_theme, name='edit_theme'),
   path('delete/<int:pk>/', views.delete_theme, name='delete_theme'),
]
