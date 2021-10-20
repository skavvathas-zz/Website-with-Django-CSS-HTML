from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html")

def qubits_view(request, *args, **kwargs):
    return render(request, "qubits.html")

def tradiotional_computing_view(request, *args, **kwargs):
    return render(request, "traditional_computing.html")   

def quantum_computing_view(request, *args, **kwargs):
    return render(request, "quantum_computing.html")

def quantum_applications_view(request, *args, **kwargs):
    return render(request, "quantum_applications.html")

def quantum_errors_view(request, *args, **kwargs):
    return render(request, "quantum_errors.html")

def quantum_supremacy_view(request, *args, **kwargs):
    return render(request, "quantum_supremacy.html")

def quantum_programming_view(request, *args, **kwargs):
    return render(request, "quantum_programming.html")
