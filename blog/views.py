from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.generic.edit import UpdateView, DeleteView

class PostListView(View):
    def get(self, request, *args, **kwargs):
        post = Post.objects.all().order_by('-timeStamp')
        form = PostForm()

        context = {
            'post_list': post,
            'form': form,
        }

        return render (request, 'blog/post_list.html', context)
    
    def post(self, request, *args, **kwargs):
        post = Post.objects.all().order_by('-timeStamp')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': post,
            'form': form,
        }

        return render (request, 'blog/post_list.html', context)

class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        context = {
            'post': post,
            'form': form,
        }

        return render(request, 'blog/post_detail.html', context)

class PostEditView(UpdateView):
    model = Post
    fields = ['title', 'contents']
    template_name = 'blog/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk':pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post-list')
