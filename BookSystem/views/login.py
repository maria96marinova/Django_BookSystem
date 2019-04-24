from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect

from BookSystem.forms.login import LogInForm
from django.contrib.auth import authenticate, login


class LogIn(View):

    form_class = LogInForm

    def get(self, request):
        login_form = LogInForm()
        context = {'form': login_form}
        return render(request, "login.html", context)

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(request.POST)
        if login_form.is_valid():
            user = authenticate(request, username=login_form.cleaned_data['username'],
                                password=login_form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                next = request.POST.get('next', '/')
                if next == '':
                    next = '/'
                return HttpResponseRedirect(next)
        else:
            return redirect('home')


