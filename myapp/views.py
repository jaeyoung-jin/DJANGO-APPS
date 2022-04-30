from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('''
    <h1></h1>


    ''')

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!' + id)