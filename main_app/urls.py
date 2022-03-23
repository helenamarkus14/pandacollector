from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
   	path('pandas/', views.PandaList.as_view(), name="panda-list"), 
    path('pandas/new/', views.Panda_Create.as_view(), name="panda_create"),
    path('pandas/<int:pk>/', views.Panda_Detail.as_view(), name ="panda_detail"),
    path('panda/<int:pk>/update', views.Panda_Update.as_view(), name = "panda_update"),
    path('panda/<int:pk>delete', views.Panda_Delete.as_view(), name="panda_delete"), # <- here we have added the new path
]