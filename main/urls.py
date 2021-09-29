from main import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('add-tractor/', views.addtractor, name='addtractor'),
    path('all-tractors/', views.alltractors, name='alltractors'),
    path('tractor-details/<int:id>/', views.tractor_details, name='tractor_details'),
]