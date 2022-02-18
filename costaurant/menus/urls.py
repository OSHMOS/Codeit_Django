from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<str:food>/', views.food_detail),  # 우아한 URL(장고의 동적 URL)
]
