from django.urls import path

from . import views

app_name = "calculator"

urlpatterns = [
    path('', views.calculator_view, name="form"),
]
