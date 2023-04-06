from django.urls import path
from app_index import views

urlpatterns = [
    path('', views.index)
]
