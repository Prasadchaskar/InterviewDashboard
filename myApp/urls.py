from django.urls import path
from . import views
# from . views import Update
urlpatterns = [
    path('',views.home,name="home"),
    path('createsched',views.Interviewschedul,name="createsched"),
    path('update/<int:id>/',views.update,name='update'),
    path('search_name',views.Search,name="search_name"),
    path('schedul_anyway',views.Schedul_anyway,name="schedul_anyway"),
]