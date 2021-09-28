from django.urls import path,include
from . import views
# from . views import Update
urlpatterns = [
    path('',views.home,name="home"),
    path('createsched',views.Interviewschedul,name="createsched"),
    path('update/<int:id>/',views.update,name='update'),
    # path('update/<int:pk>',Update.as_view(),name="update")
]