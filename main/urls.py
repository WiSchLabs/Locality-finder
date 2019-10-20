from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from main.views import (WorldBorderCreateView, WorldBorderDetailJsonView, WorldBorderDetailView, WorldBorderListView,
                        WorldBorderUpdateView, WorldBorderListJsonView)

app_name = "main"

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='index'),

    path('geo/', TemplateView.as_view(template_name='main/geo.html'), name='geo'),

    path('borders/create/', WorldBorderCreateView.as_view(), name='worldborder_create'),
    path('borders/list/', WorldBorderListView.as_view(), name='worldborder_list'),

    path('borders/update/<str:worldborder_slug>/', WorldBorderUpdateView.as_view(), name='worldborder_update'),

    path('borders/json/', WorldBorderListJsonView.as_view(), name='worldborder_list_json'),
    path('borders/json/<str:worldborder_slug>/', WorldBorderDetailJsonView.as_view(), name='worldborder_detail_json'),

    path('borders/<str:worldborder_slug>/', WorldBorderDetailView.as_view(), name='worldborder_detail'),
]
