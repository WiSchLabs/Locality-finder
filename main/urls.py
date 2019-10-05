from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),

    url(r'^geo/$', TemplateView.as_view(template_name='main/geo.html'), name='geo'),
]
