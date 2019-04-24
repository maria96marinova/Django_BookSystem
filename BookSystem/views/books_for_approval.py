from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from BookSystem.services import BookService


class BooksForApproval(View):

    @method_decorator(login_required)
    def get(self, request):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        books = BookService.getBooksForApproval()
        booksModels = list(map(self.customMapper, books))
        successApproved = request.session.get('successApproved', None)
        errorApproved = request.session.get('errorApproved', None)

        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'books': booksModels, 'successApproved': successApproved,
                   'errorApproved': errorApproved,  'adminUsers': adminUsers}

        if successApproved:
            del request.session['successApproved']

        if errorApproved:
            del request.session['errorApproved']

        return render(request, "books_for_approval.html", context)

    def customMapper(self, a):
        a = BookViewModel(id=a.id, title=a.title, description=a.description,
                          date=a.publication_date,
                          category=a.category.name, publisher=a.publisher.name)

        return a


class BookViewModel:

    def __init__(self, id, title, description, date, category, publisher):
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.category = category
        self.publisher = publisher

