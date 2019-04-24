from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views import View

from django.shortcuts import render, redirect

from BookSystem.forms.add_author import AuthorForm
from BookSystem.services import AuthorService


class AddAuthor(View):
    form_class = AuthorForm

    @method_decorator(login_required)
    def get(self, request):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        author_form = AuthorForm()

        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'form': author_form,  'adminUsers': adminUsers}
        return render(request, "add_author.html", context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        author_form = self.form_class(request.POST)
        if author_form.is_valid():
            AuthorService.add(author_form.cleaned_data['first_name'], author_form.cleaned_data['last_name'],
                              author_form.cleaned_data['type'])
            return redirect('author')
        else:
            return redirect('home')