from typing import ValuesView
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('createsched',views.Interviewschedul,name="createsched"),
]