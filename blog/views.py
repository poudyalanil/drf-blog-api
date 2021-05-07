from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Category, Blog, Tag

# Create your views here.
def check_api(request):
    resp = {
        "api_name":"drf-api",
        'version':"0.01",
        'status':"good"
        }
    return JsonResponse(resp)