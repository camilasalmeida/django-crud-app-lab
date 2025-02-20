from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resorts/', views.resort_index, name='resort-index'),

    path('resorts/<int:resort_id>/', views.resort_detail, name='resort-detail'),
    path('resorts/create/', views.ResortCreate.as_view(), name='resort-create'),
    path('resorts/<int:pk>/update/', views.ResortUpdate.as_view(), name='resort-update'),
    path('resorts/<int:pk>/delete/', views.ResortDelete.as_view(), name='resort-delete'),

]

