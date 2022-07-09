from django.urls import path

from . import views

app_name = "algoviewer"

urlpatterns = [
    path('', views.algoviewer_home, name="home"),
]
