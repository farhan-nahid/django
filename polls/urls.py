from django.urls import path
from . import views

urlpatterns = [
    path('', views.get, name='get root view'),
]
