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
]

