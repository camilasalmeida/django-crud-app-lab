from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/signup/', views.signup, name='signup'),

    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('resorts/', views.resort_index, name='resort-index'),
    path('resorts/<int:resort_id>/', views.resort_detail, name='resort-detail'),
    path('resorts/create/', views.ResortCreate.as_view(), name='resort-create'),
    path('resorts/<int:pk>/update/', views.ResortUpdate.as_view(), name='resort-update'),
    path('resorts/<int:pk>/delete/', views.ResortDelete.as_view(), name='resort-delete'),
    path('resorts/<int:resort_id>/add-trip/', views.add_trip, name='add-trip'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trip-update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trip-delete'),
]

