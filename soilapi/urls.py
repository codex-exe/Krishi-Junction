from django.urls import path

from . import views

urlpatterns = [
    path('soiltest/', views.test, name='index'),
    path("npkvalue/", views.npkvalue),
    path("crop_pred/", views.crop_pred)
]