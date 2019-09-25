from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request=request, template_name='main/index.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            if user is not None:
                messages.success(request, f"New Account created: {username}")
                login(request, user)
            else:
                return redirect("main:login")
            return redirect("main:index")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = UserCreationForm()
    return render(request=request,
                  template_name='main/register.html',
                  context={'form': form}
                  )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main:index")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="main/login.html",
                          context={"form": form})
    else:
        form = AuthenticationForm()
        return render(request=request,
                      template_name='main/login.html',
                      context={'form': form}
                      )


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:index")


def profile(request):
    return render(request=request, template_name='main/index.html')
