from django.urls import path
from . import views

urlpatterns = [
    path('admin_view/', views.admin_view, name='admin_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]
