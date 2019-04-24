from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from BookSystem.services import PublisherService


class Publisher(View):

    @method_decorator(login_required)
    def get(self, request):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        publishers = PublisherService.getAll()
        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'publishers': publishers, 'adminUsers': adminUsers}
        return render(request, "publishers.html", context)

