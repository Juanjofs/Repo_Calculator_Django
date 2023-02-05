from django.urls import path
from app import views

urlpatterns = [
    path('sumar/<int:op1>/<int:op2>', views.add),
    path('restar/<int:op1>/<int:op2>', views.sub),
    path('multiplicar/<int:op1>/<int:op2>', views.mul),
    path('dividir/<int:op1>/<int:op2>', views.div),
]