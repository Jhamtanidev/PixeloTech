from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    
    path('', views.login_view, name='login'),
    path('register/',views.register_view,name='register'),
    path('otp/',views.otp_view,name='otp'),
    path('dashboard/',views.dashboard_view,name='dashboard')
    ]