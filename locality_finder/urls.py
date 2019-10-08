"""locality_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from main import views

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),

    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^accounts/logged-out/', TemplateView.as_view(template_name='main/logged_out.html'), name='logged_out'),
    url(r'^accounts/profile/(?P<username>[a-zA-Z0-9]+)/$', views.get_user_profile, name='profile'),
]
