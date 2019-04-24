from django.contrib.auth.models import Group
from django.views import View
from django.shortcuts import render
from BookSystem.services import CategoryService, BookService


class HomeView(View):

    def get(self, request):

        categories = CategoryService.getAll()
        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'categories': categories, 'adminUsers': adminUsers}


        return render(request, "home.html", context)



