from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Post
from django.views import View

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        data = [{"id": post.id, "content": post.content, "image": post.image.url} for post in posts]
        return JsonResponse(data, safe=False)

class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = {"id": post.id, "content": post.content, "image": post.image.url}
        return JsonResponse(data)

class PostCreateView(View):
    def post(self, request):
        # Logic for creating a new post
        pass

class PostUpdateView(View):
    def post(self, request, pk):
        # Logic for updating an existing post
        pass

class PostDeleteView(View):
    def post(self, request, pk):
        # Logic for deleting a post
        pass