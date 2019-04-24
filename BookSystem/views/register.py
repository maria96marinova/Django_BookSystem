from django.views import View
from django.shortcuts import render, redirect

from BookSystem.forms.register import RegisterForm
from BookSystem.services import UserService


class Register(View):

    form_class = RegisterForm

    def get(self, request):
        register_form = RegisterForm()
        context = {'form': register_form}
        return render(request, "register.html", context)

    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST)
        if register_form.is_valid():
            UserService.add_user(register_form.cleaned_data['first_name'], register_form.cleaned_data['last_name'],
                                 register_form.cleaned_data['email'],
                              register_form.cleaned_data['country'], register_form.cleaned_data['username'],
                              register_form.cleaned_data['password'])

            return redirect('book')
        else:
            return redirect('home')
