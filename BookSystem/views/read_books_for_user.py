from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render

from BookSystem.services import BookService


class UserReadBooks(View):

    @method_decorator(login_required)
    def get(self, request):
        books = BookService.getReadBooksForUser(request.user.id)
        a = books[0]
        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'books': books,  'adminUsers': adminUsers}
        return render(request, "user_read_books.html", context)


