from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(req, op1, op2):
    return HttpResponse(op1+op2)


def sub(req, op1, op2):
    return HttpResponse(op1-op2)


def mul(req, op1, op2):
    return HttpResponse(op1*op2)


def div(req, op1, op2):
    try:
        resultado = op1/op2
    except ZeroDivisionError:
        resultado = "No se puede dividir entre cero(0)"
    return HttpResponse(resultado)