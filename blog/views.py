from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Category, Blog, Tag
from datetime import  datetime

# Create your views here.
def check_api(request):
    resp = {
        'date':datetime.now,
        "api_name":"drf-api",
        'version':"0.01",
        'status':"good"
        
        }
    return JsonResponse(resp)