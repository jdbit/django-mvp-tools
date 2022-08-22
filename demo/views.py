from django.shortcuts import render
from .models import Post
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class PostDetailView(DetailView):
    model = Post


class TagDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    paginate_by = 21
