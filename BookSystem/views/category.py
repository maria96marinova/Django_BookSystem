from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect

import BookSystem
from BookSystem.models import Category
from BookSystem.services import CategoryService


class Category(View):

    @method_decorator(login_required)
    def get(self, request):

        categories = CategoryService.getAll()

        categories = list(map(self.customMapper, categories))

        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'categories': categories,  'adminUsers': adminUsers}
        return render(request, "categories.html", context)

    def customMapper(self, c):
        b = BookSystem.models.Book.book_with_category.all()
        c = CategoryViewModel(c.id, c.name, BookSystem.models.Book.book_with_category.all()
                              .filter(category__name=c.name).count())
        return c

class CategoryViewModel:

    def __init__(self, id, name, num_books):
        self.id = id
        self.name = name
        self.num_books = num_books


