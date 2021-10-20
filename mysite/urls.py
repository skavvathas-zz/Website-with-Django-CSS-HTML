"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('home/', views.home_view,),
    path('qubits/', views.qubits_view, name="qubits"),
    path('traditional_computing/', views.tradiotional_computing_view, name="traditional_computing"),
    path('quantum_computing/', views.quantum_computing_view, name="quantum_computing"),
    path('quantum_applications/', views.quantum_applications_view, name="quantum_applications"),
    path('quantum_errors/', views.quantum_errors_view, name="quantum_errors"),
    path('quantum_supremacy/', views.quantum_supremacy_view, name="quantum_supremacy"),
    path('quantum_programming/', views.quantum_programming_view, name="quantum_programming"),
    path('admin/', admin.site.urls),
]
