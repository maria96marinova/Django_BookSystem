from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect

from BookSystem.forms.add_publisher import PublisherForm
from BookSystem.services import PublisherService


class AddPublisher(View):
    form_class = PublisherForm

    @method_decorator(login_required)
    def get(self, request):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        publisher_form = PublisherForm()
        adminUsers = Group.objects.get(name='ADMIN').user_set.all()
        context = {'form': publisher_form, 'adminUsers': adminUsers}
        return render(request, "add_publisher.html", context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.user.groups.filter(name='ADMIN').count() == 0:
            return redirect('home')

        publisher_form = self.form_class(request.POST)
        if publisher_form.is_valid():
            PublisherService.add(publisher_form.cleaned_data['name'], publisher_form.cleaned_data['country'])
            return redirect('publisher')
        else:
            return redirect('home')