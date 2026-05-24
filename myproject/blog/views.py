from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import StudentSerializer

@login_required
def home(request):
    # Fetch all posts
    posts = Post.objects.all()
    return render(request, "blog/home.html", {"posts": posts})

@login_required
def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            Post.objects.create(title=title, content=content)

    return redirect("/")

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("/")

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("/")

    return render(request, "blog/edit.html", {"post": post})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "blog/login.html", {"error": "Invalid credentials"})

    return render(request, "blog/login.html")

def logout_view(request):
    logout(request)
    return redirect("/login/")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_api(request):
    return Response({"message": "You are authenticated"})