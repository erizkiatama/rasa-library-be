from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookListAPIView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailAPIView.as_view(), name='book_detail'),
    path('types/', views.book_type_list, name='book_type_list')
]
