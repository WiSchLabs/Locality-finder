from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from djgeojson.views import GeoJSONLayerView

from main.forms import WorldBorderCreateForm
from main.models import WorldBorder


def index(request):
    return render(request=request, template_name='main/index.html')


def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'main/profile.html', {"user": user})


class WorldBorderCreateView(CreateView):
    form_class = WorldBorderCreateForm
    template_name = 'main/worldborder_create.html'
    success_url = reverse_lazy('main:worldborder_list')


class WorldBorderUpdateView(UpdateView):
    form_class = WorldBorderCreateForm
    template_name = 'main/worldborder_update.html'
    success_url = reverse_lazy('main:worldborder_list')
    context_object_name = 'world_border'
    slug_field = 'worldborder_slug'
    slug_url_kwarg = 'worldborder_slug'

    def get_queryset(self):
        b = WorldBorder.objects.get(worldborder_slug=self.kwargs['worldborder_slug'])
        return WorldBorder.objects.filter(name=b.name)


class WorldBorderListView(ListView):
    model = WorldBorder
    context_object_name = 'world_borders'
    paginate_by = 15
    ordering = 'name'


class WorldBorderDetailJsonView(GeoJSONLayerView):
    model = WorldBorder
    slug_field = 'worldborder_slug'
    slug_url_kwarg = 'worldborder_slug'

    def get_queryset(self):
        world_border = WorldBorder.objects.get(worldborder_slug=self.kwargs['worldborder_slug'])
        return WorldBorder.objects.filter(name=world_border)


class WorldBorderDetailView(DetailView):
    model = WorldBorder
    context_object_name = 'world_border'
    slug_field = 'worldborder_slug'
    slug_url_kwarg = 'worldborder_slug'

    def get_queryset(self):
        b = WorldBorder.objects.get(worldborder_slug=self.kwargs['worldborder_slug'])
        return WorldBorder.objects.filter(name=b.name)
