from django.urls import path

from query_apis.api_football import views

app_name = "football"

urlpatterns = [
    path('', views.index)
]
