from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views import View

from BookSystem.forms.add_category import CategoryForm
from BookSystem.services import CategoryService
from django.shortcuts import render, redirect


class AddCategory(View):
    form_class = CategoryForm

    @method_decorator(login_required)
    def get(self, request):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        category_form = CategoryForm()
        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'form': category_form, 'adminUsers': adminUsers}
        return render(request, "add_category.html", context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        category_form = self.form_class(request.POST)
        if category_form.is_valid():
            CategoryService.add(category_form.cleaned_data['name'])
            return redirect('category')
        else:
            return redirect('home')