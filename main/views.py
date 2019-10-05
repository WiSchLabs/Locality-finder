from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    return render(request=request, template_name='main/index.html')


def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'main/profile.html', {"user": user})
