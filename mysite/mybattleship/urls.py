from django.urls import path
from . import views

urlpatterns = [
    path("create_battlefield", views.create_battlefield, name="create_battlefield"),
    path("show_battlefield/<pk>", views.show_battlefield, name="show_battlefield"),
]
