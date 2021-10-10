from django.urls import path

from . import views

urlpatterns = [
    path('get_res/', views.get_image, name='index'),
]