from rest_framework import serializers

from .models import Book, BookVolume, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookVolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookVolume
        fields = ['id', 'volume', 'image_url']


class ListBookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    type = serializers.SerializerMethodField()
    total_volumes = serializers.SerializerMethodField()

    def get_total_volumes(self, obj):
        if obj.has_volumes:
            return obj.book_volumes.count()
        return 0

    def get_type(self, obj):
        return obj.BookType(obj.type).label

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'type',
            'has_volumes',
            'image_url',
            'total_volumes',
        ]
        depth = 1


class RetrieveBookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    type = serializers.SerializerMethodField()
    all_volumes = BookVolumeSerializer(read_only=True, many=True)

    def get_type(self, obj):
        return obj.BookType(obj.type).label

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'type',
            'has_volumes',
            'image_url',
            'all_volumes'
        ]
        depth = 1
