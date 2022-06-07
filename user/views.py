from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import signup

class register(generic.CreateView):
    form_class = signup
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')