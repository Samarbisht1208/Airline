from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login_kr_rha_hu"))
    return render(request, "users/user.html")
    

def login_view(request):
    if request.method == "POST":
        username_variable = request.POST["username_daal"]
        password_variable = request.POST["password_daal"]
        # here authenticate check if username and password is correct and then give the user
        user = authenticate(request, username=username_variable, password=password_variable)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index_users"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out."
    })