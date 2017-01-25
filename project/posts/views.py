from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from posts.models import Post
from django.views.generic.edit import DeleteView

from django.views.generic.edit import CreateView
# Create your views here.

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title','slug', 'image', 'content']

class PostDeleteView(DeleteView):
    model = Post
