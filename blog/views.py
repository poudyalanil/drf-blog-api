from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Category, Blog, Tag
from datetime import  datetime
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import  Blog_Serializer,Category_Serializer,Tag_Serializer

# Create your views here.
def check_api(request):
    resp = {
        "api_name":"drf-api",
        'version':"0.01",
        'status':"good",
        'country':'Nepal',
        }
    return JsonResponse(resp)

def blog_list(request):
    if request.get:
        blogs = Blog.objects.all()
        serializer = Blog_Serializer(blogs,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif  request.post:
        data = JSONParser().parse(request)
        serializer = Blog_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        else:
            return JsonResponse(serializer.errors,status = 400)
        

