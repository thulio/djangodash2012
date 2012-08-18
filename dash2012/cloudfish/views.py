from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect


def index(request):
    if request.user.is_authenticated():
        return render(request, 'index_loggedin.html', {'greetings':'Hi!'})
    return render(request, 'index.html')


@login_required
def account(request):
    return render(request, 'account.html', {'active_account': 'active'})


@login_required
def servers(request):
    return render(request, 'servers.html', {'active_servers': 'active'})

@csrf_protect
def register(request):
    c = {}
    if request.POST:
        username = email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm-password']

        if User.objects.filter(email=username):
            c["errors"] = "This email is already in use."
            return render(request, "register.html", c)

        new_user = User.objects.create_user(username, email, password)
        new_user.save()

        user = authenticate(username=username, password=password)
        login(request, user)

    return render(request, 'register.html', c)