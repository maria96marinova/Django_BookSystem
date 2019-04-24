from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from BookSystem.forms.add_book import BookForm
from BookSystem.services import BookService


class SuggestBooks(View):
    form_class = BookForm

    @method_decorator(login_required)
    def get(self, request):

        book_form = BookForm()
        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'form': book_form, 'adminUsers':adminUsers}
        return render(request, "suggest_book.html", context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        book_form = self.form_class(request.POST)
        if book_form.is_valid():
            BookService.add(book_form.cleaned_data['title'], book_form.cleaned_data['description'],
                            book_form.cleaned_data['publication_date'], book_form.cleaned_data['category'],
                            book_form.cleaned_data['publisher'], book_form.cleaned_data['authors'],
                            isApproved=False)

            return redirect('book_for_user')
        else:
            return redirect('book')