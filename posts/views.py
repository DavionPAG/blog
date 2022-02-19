from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from posts.models import Post

# Create your views here.

class PostListView(ListView):
  template_name = "post_list.html"
  model = Post

class PostDetailView(DetailView):
  template_name = "post_detail.html"
  model = Post

class PostCreateView(CreateView):
  template_name = 'post_create.html'
  model = Post
  fields = ['title', 'author', 'body']

class PostUpdateView(UpdateView):
  template_name = 'post_update.html'
  model = Post
  fields = ['title', 'body']

class PostDeleteView(DeleteView):
  template_name = 'post_delete.html'
  model = Post
  success_url = reverse_lazy('post_list')