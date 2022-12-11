from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page ,name='login'),
    path('logout/', views.logout_user ,name='logout'),
    path('register/', views.register_user ,name='register'),
    path('', views.home ,name='home'),
    path('room/<int:pk>/',views.room,name='room'),
    path('profile/<int:pk>/',views.user_profile,name='profile'),
    path('update_user/', views.update_user ,name='update_user'),
    path('create_room/',views.create_room,name='create_room'),
    path('update_room/<int:pk>/',views.update_room,name='update_room'),
    path('delete_room/<int:pk>/',views.delete_room,name='delete_room'),
    path('delete_message/<int:pk>/',views.delete_message,name='delete_message'),
    path('topics/', views.topic_page ,name='topics'),
    path('activity/', views.activity_page ,name='activity'),
]
