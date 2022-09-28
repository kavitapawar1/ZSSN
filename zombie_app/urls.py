from django.urls import path
from zombie_app import views

urlpatterns = [
    path('survivors/', views.Survivors.as_view(), name='survivors' ),
    path('survivors/<int:id>', views.ServivorById.as_view(), name='survivor' ),
    path('survivors/reports', views.InfectedRecords.as_view(), name='reports' ),
    path('survivors/reports_noninfected', views.NonInfectedRecords.as_view(), name='reports_noninfected' ),
    
]
