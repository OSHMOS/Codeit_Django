from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.food_detail),  # 우아한 URL(장고의 동적 URL)
]
