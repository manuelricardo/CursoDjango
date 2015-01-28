#from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponse

def pruebas1(request):
	return HttpResponse('Respuesta desde pruebas1')

def Pruebas2(request):
	return HttpResponse('Respuesta desde pruebas2')

def Pruebas3(request):
	return HttpResponse('Respuesta desde pruebas3')