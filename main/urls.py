

from django.urls import path
from . import views
from posts import views as postview

app_name = 'main'
urlpatterns = [
    path('', views.index, name="index"),
    path('<str:newmenu>/',views.newmenu, name="newmenu"),
    
]
