from django.urls import path
from . import views

urlpatterns = [
    path("", views.startup_index, name="startup_index"),
    path("<int:pk>/", views.startup_detail, name="startup_detail"),
]