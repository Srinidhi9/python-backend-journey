from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")   # safer than "home" if not named
        else:
            return render(request, "blog/login.html", {"error": "Invalid credentials"})

    return render(request, "blog/login.html")