from django.urls import path, include

app_name = "query_apis"

urlpatterns = [
    path('football/', include('query_apis.api_football.urls')),
]
