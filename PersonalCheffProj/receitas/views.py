from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse ("Sejam Bem Vindos")
# Create your views here.
