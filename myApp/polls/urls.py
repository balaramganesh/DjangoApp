from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("input/", views.input_view, name="input_view"),
    path("success/", views.success_page, name="success_page"),
]