from django.contrib.auth.models import User
from django.db import models

from BookSystem.managers import BookWithCategoryManager, AuthorWithBooks


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "categories"


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50)

    class Meta:
        db_table = "publishers"


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)

    objects = models.Manager()
    authors_with_books = AuthorWithBooks()

    class Meta:
        db_table = "authors"


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    publication_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    isApproved = models.BooleanField(default=False)

    objects = models.Manager()
    book_with_category = BookWithCategoryManager()


    class Meta:
        db_table = "books"


class Reader(models.Model):
    country = models.CharField(max_length=60, default='Bulgaria')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    class Meta:
        db_table = "readers"

