from django.urls import path

from .views import ServicosListView


urlpatterns = [
    path("", ServicosListView.as_view(), name="list"),
]