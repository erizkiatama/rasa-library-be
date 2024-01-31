from django.http import JsonResponse
from rest_framework import generics

from .models import Book
from .serializers import ListBookSerializer, RetrieveBookSerializer


class BookListAPIView(generics.ListAPIView):
    serializer_class = ListBookSerializer

    def get_queryset(self):
        """
        This view should return all books filtered by given query parameters
        """
        queryset = Book.objects.all()
        title = self.request.query_params.get('title')
        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        book_type = self.request.query_params.get('type')
        if book_type is not None:
            queryset = queryset.filter(type__exact=book_type)

        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author__name__icontains=author)

        return queryset


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = RetrieveBookSerializer


def book_type_list(request):
    return JsonResponse(
        {'types': [{'key': choice[0], 'text': choice[1]} for choice in Book.BookType.choices]}
    )

