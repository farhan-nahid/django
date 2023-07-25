from django.urls import path
from . import views

urlpatterns = [
    path('', views.get, name='get root view'),
    path('<str:question_id>/', views.detail, name='details view')
]
