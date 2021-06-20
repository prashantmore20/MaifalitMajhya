from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin
from blog.models import Post

# Create your views here.

class Index(View):
    def get(self, request, *args, **kwargs):
        logged_in_user = request.user
        posts = Post.objects.filter().order_by('-timeStamp')[:3]

        context = {
            'post_list': posts,
        }
        
        return render(request, 'landing/index.html', context)
