from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

class blog(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-date']

class detail(DetailView):
    model = Post
    template_name = 'detail.html'

class post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('blog')

class update(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = UpdateForm
    success_url = reverse_lazy('blog')

class delete(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')