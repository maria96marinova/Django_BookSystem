from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render

from BookSystem.services import BookService


class Book(View):

    @method_decorator(login_required)
    def get(self, request):
        books = BookService.getAll()
        a = books[0]
        booksModels = list(map(self.customMapper, books))

        adminUsers = Group.objects.get(name='ADMIN').user_set.all()

        successEdited = request.session.get('successEdited', None)
        errorEdited = request.session.get('errorEdited', None)


        if successEdited:
            del request.session['successEdited']

        if errorEdited:
            del request.session['errorEdited']

        context = {'books': booksModels, 'adminUsers': adminUsers, 'successEdited': successEdited,
                   'errorEdited': errorEdited}

        return render(request, "books.html", context)

    def customMapper(self, a):
        a = BookViewModel(id = a.id, title=a.title, description=a.description,
                          date = a.publication_date,
                          category=a.category.name, publisher = a.publisher.name, authors=a.authors)

        return a



class BookViewModel:

    def __init__(self, id, title, description, date, category, publisher, authors):

        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.category = category
        self.publisher = publisher
        self.authors = authors

