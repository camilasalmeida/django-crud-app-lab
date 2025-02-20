from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resorts/', views.resort_index, name='resort-index'),

     path('resorts/<int:resort_id>/', views.resort_detail, name='resort-detail'),
     path('resorts/create/', views.ResortCreate.as_view(), name='resort-create'),

]

