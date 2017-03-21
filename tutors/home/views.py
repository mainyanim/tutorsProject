from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Subject
from django.views import generic


class HomeView(TemplateView):
    template_name = 'home/home.html'
    paginate_by = 10
    def get(self, request):
        users = User.objects.all()

        args = {'users': users }
        return render(request, self.template_name, args)
