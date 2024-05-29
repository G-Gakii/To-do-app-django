from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepage,name='homepage'),
    path('register/',views.registerpage,name='register'),
    path('login/',views.loginpage,name='logIn'),
    path('delete/<str:name>/',views.deleteTask, name='delete'),
    path('update/<str:name>/',views.updateTask,name='update'),
    path('logout/',views.logOut,name='logOut'),
]
