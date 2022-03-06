

from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [

    path('list/',views.index, name="list"),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('eidt/<int:post_id>',views.edit, name="edit"),
    path('delete/<int:post_id>',views.delete, name ="delete"),
    path('search/<str:keyword>',views.search, name = "search")
]
