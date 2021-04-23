from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Category, Blog, Tag
from datetime import  datetime
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
def check_api(request):
    resp = {
        "api_name":"drf-api",
        'version':"0.01",
        'status':"good",
        'country':'Nepal',
        }
    return JsonResponse(resp)

