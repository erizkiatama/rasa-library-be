from django.db import models


class Author(models.Model):

    class Meta:
        db_table = 'authors'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Book(models.Model):

    class Meta:
        db_table = 'books'

    class BookType(models.TextChoices):
        COMIC = "COMIC", "Comic"
        NOVEL = "NOVEL", "Novel"

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=25, choices=BookType.choices)
    has_volumes = models.BooleanField(default=False)
    image_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BookVolume(models.Model):

    class Meta:
        db_table = 'book_volumes'

    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='volumes')
    volume = models.IntegerField()
    image_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.book, self.volume)