from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.get_rooms, name="rooms")
]