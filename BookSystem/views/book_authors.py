from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views.generic.base import View

from BookSystem.services import BookService


class BookAuthors(View):

    def get(self, request, id):
        authors = BookService.getBookAuthors(id)
        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'authors':authors, 'adminUsers': adminUsers}
        return render(request, "books_authors.html", context)

