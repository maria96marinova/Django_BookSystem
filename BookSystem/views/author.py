from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views import View

import BookSystem
from BookSystem.models import Author
from BookSystem.services import AuthorService
from django.shortcuts import render, redirect


class Author(View):

    @method_decorator(login_required)
    def get(self, request):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        authors = AuthorService.getAll()
        authors = map(self.customMapper, authors)

        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'authors': authors,  'adminUsers': adminUsers}
        return render(request, "authors.html", context)

    def customMapper(self,a):

        author = AuthorViewModel(a.first_name, a.last_name, a.type,
                                 BookSystem.models.Author.authors_with_books.get_books(a.id))
        return author

class AuthorViewModel:

    def __init__(self, first_name, last_name, type, num_books):
        self.first_name = first_name
        self.last_name = last_name
        self.type = type
        self.num_books = num_books


