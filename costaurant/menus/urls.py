from . import views
from django.urls import path

urlpatterns = [
    path('menus/', views.index)
]
