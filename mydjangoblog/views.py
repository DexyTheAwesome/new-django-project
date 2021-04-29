# from django.http import HttpResponse
# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.forms import ModelForm, widgets


# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
   
    
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
    
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'new_comment.html'
    widgets = {
            'post': widgets.HiddenInput
        }

    def form_valid(self, form ):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


