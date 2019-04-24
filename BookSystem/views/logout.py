from django.shortcuts import redirect
from django.views import View
from django.contrib.auth import logout


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('home')

