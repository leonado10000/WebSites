from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainPage, name="mainPage"),
    path('add', views.addPage, name="add")
]