from django.urls import path

from . import views

urlpatterns = [
    path('soiltest/', views.test, name='index'),
    path("npkvalue/", views.npkvalue)
]