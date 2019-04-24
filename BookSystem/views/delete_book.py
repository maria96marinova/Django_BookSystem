from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View

from BookSystem.services import BookService


class DeleteBook(View):

    @method_decorator(login_required)
    def post(self, request):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        book_id = request.POST['book_id']
        BookService.deleteBook(book_id)
        return redirect('book')