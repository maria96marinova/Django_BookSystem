from django.db import models
from django.db.models import Count


class BookWithCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('category').annotate(Count('id'))

class AuthorWithBooks(models.Manager):

    def get_books(self, author_id):
        return super().get_queryset().get(pk= author_id).book_set.all().count()





