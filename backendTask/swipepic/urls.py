from django.urls import path
from . import views

app_name = 'swipepic'

urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/',views.history,name='history'),
    
    ]

