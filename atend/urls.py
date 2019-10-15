from django.urls import path 
from .import views


urlpatterns = [
   
   
    path('member/<str:email>/',views.makeAttendence,name="email"),
]