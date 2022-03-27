from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
   	path('pandas/', views.PandaList.as_view(), name="panda-list"), 
    path('pandas/new/', views.Panda_Create.as_view(), name="panda_create"),
    path('pandas/<int:pk>/', views.Panda_Detail.as_view(), name ="panda_detail"),
    path('panda/<int:pk>/update', views.Panda_Update.as_view(), name = "panda_update"),
    path('panda/<int:pk>/delete', views.Panda_Delete.as_view(), name="panda_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('pandatoys/', views.pandatoys_index, name="pandatoys_index"),# <- here we have added the new path
    path('pandatoys/<int:pandatoy_id>/', views.pandatoys_show, name="pandatoys_show"),# <- here we have added the new path
    path('pandatoys/create/', views.PandaToyCreate.as_view(), name="pandatoys_create"),# <- here we have added the new path
    path('pandatoys/<int:pk>/update/', views.PandaToyUpdate.as_view(), name="pandatoys_update"),# <- here we have added the new path
    path('pandatoys/<int:pk>/delete/', views.PandaToyDelete.as_view(), name="pandatoys_delete"),
    
    path('pandasnacks/', views.pandasnacks_index, name="pandasnacks_index"),# <- here we have added the new path
    path('pandasnacks/<int:pandasnack_id>/', views.pandasnacks_show, name="pandasnacks_show"),# <- here we have added the new path
    path('pandasnacks/create/', views.PandaSnackCreate.as_view(), name="pandasnacks_create"),# <- here we have added the new path
    path('pandasnacks/<int:pk>/update/', views.PandaSnackUpdate.as_view(), name="pandasnacks_update"),# <- here we have added the new path
    path('pandasnacks/<int:pk>/delete/', views.PandaSnackDelete.as_view(), name="pandasnacks_delete"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]