from django.urls import path
from . import views
from .views import (
    login_view, dashboard, logout_view, 
    patient_list, patient_add, patient_detail, patient_delete
)

urlpatterns = [
    path('', views.overview, name='overview'),
  
    path("login/", login_view, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.patient_add, name='patient_add'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path("patients/delete/<int:pk>/", patient_delete, name="patient_delete"),

    path('doctor/', views.doctor_portal, name='doctor_portal'),
    path('patient/', views.patient_portal, name='patient_portal'),
    path('tele/', views.tele_portal, name='tele_portal'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('patient/<int:pk>/pdf/', views.patient_pdf, name='patient_pdf'),
]

