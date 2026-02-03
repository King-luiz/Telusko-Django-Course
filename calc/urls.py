from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about.html', views.about, name='about'),
    path('blue.html', views.blue, name='blue'),
    path('block.html', views.block, name='block'),
    path('result.html', views.result, name='result'),
    path('add', views.add, name='add'),
    
    
    ]