from django.urls import path
from . import views

app_name = 'clinic_admin'

urlpatterns = [
    # Admin Dashboard
    path('', views.admin_dashboard, name='dashboard'),
    
    # Doctors Management
    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('doctors/create/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/edit/', views.DoctorUpdateView.as_view(), name='doctor_edit'),
    path('doctors/<int:pk>/delete/', views.DoctorDeleteView.as_view(), name='doctor_delete'),
    
    # Schedules Management
    path('schedules/', views.manage_schedules, name='schedules'),
    path('schedules/<int:doctor_id>/create/', views.create_availability, name='availability_create'),
    
    # Slots Management
    path('slots/', views.manage_slots, name='slots'),
    path('slots/generate/', views.generate_slots, name='slot_generate'),
    
    # Appointments Management
    path('appointments/', views.manage_appointments, name='appointments'),
]
