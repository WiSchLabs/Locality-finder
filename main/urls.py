from django.conf.urls import url
from django.urls import path
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from main.models import WorldBorder
from main.views import (WorldBorderCreateView, WorldBorderDetailJsonView, WorldBorderDetailView, WorldBorderListView,
                        WorldBorderUpdateView)

from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name='index'),

    url(r'^geo/$', TemplateView.as_view(template_name='main/geo.html'), name='geo'),

    path('borders/create/', WorldBorderCreateView.as_view(), name='worldborder_create'),
    path('borders/list/', WorldBorderListView.as_view(), name='worldborder_list'),

    path('borders/update/<str:worldborder_slug>/', WorldBorderUpdateView.as_view(), name='worldborder_update'),

    path('borders/json/', cache_page(60 * 15)(GeoJSONLayerView.as_view(model=WorldBorder, geometry_field='mpoly')), name='worldborder_list_json'),
    path('borders/json/<str:worldborder_slug>/', cache_page(60 * 15)(WorldBorderDetailJsonView.as_view(model=WorldBorder, geometry_field='mpoly')), name='worldborder_detail_json'),

    path('borders/<str:worldborder_slug>/', WorldBorderDetailView.as_view(), name='worldborder_detail'),
]
