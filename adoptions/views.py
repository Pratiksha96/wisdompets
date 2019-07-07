from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse('<p>Home view</p>')

def pet_detail(request,id):
	return HttpResponse('<p>Pet detail view with id %s </p>' %id)
