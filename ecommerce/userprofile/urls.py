from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor_detail'),
]