from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("order/", views.input_order, name="input_order"),
    path("success/", views.success_page, name="success_page"),
]