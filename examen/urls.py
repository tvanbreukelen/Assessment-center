from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='examen-home'),
    path('v1', views.v1, name='examen-v1'),
    path('v2', views.v2, name='examen-v2'),
    path('v3', views.v3, name='examen-v3'),
    path('v4', views.v4, name='examen-v4'),
    path('v5', views.v5, name='examen-v5'),
    path('v6', views.v6, name='examen-v6'),
    path('v7', views.v7, name='examen-v7'),
    path('v8', views.v8, name='examen-v8'),
    path('v9', views.v9, name='examen-v9'),
    path('v10', views.v10, name='examen-v10'),
    path('v11', views.v11, name='examen-v11'),
] 