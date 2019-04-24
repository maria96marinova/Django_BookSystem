from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from BookSystem.forms.edit_book import EditBookForm
from BookSystem.services import BookService, AuthorService, PublisherService, CategoryService


class EditBook(View):

    @method_decorator(login_required)
    def get(self, request, id):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        book = BookService.getBook(id)

        categories = CategoryService.getAll()

        authorsForBook = book.authors.all()

        authors = AuthorService.getAll()

        publishers = PublisherService.getAll()

        adminUsers = Group.objects.get(name='ADMIN').user_set.all()

        context = {'book': book, 'authors':authors, 'categories':categories,
                   'authorsForBook': authorsForBook, 'publishers':publishers, 'adminUsers': adminUsers}
        return render(request, "edit_book.html", context)

    @method_decorator(login_required)
    def post(self, request, id):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        success = BookService.editBook(id, request.POST.get('title'), request.POST.get('description'), request.POST.get('publication_date'),
                                       request.POST.get('categoryId'), request.POST.get('publisherId'), request.POST.get('authorsIds'))

        if success == False:
            request.session['errorEdited'] = "This book does not exist"

        else:
            request.session['successEdited'] = "Successfully edited book"


        return redirect('book')
