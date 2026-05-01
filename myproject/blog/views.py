from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
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