from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View

from BookSystem.services import BookService


class ApproveBook(View):

    @method_decorator(login_required)
    def post(self, request):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        id = request.POST.get('book_id')
        success = BookService.approveBook(id)

        if success == False:
            request.session['errorApproved'] = "This book does not exist"

        else:
            request.session['successApproved'] = "Successfully approved book"

        return redirect('books_for_approval')


