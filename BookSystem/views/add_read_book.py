from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from BookSystem.services import BookService
from django.shortcuts import redirect


class AddReadBook(View):

    @method_decorator(login_required)
    def post(self, request):

        book_id = request.POST['book_id']
        BookService.addReadBook(book_id, request.user.id)
        return redirect('home')

