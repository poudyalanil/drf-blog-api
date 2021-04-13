from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Category, Blog, Tag
from datetime import  datetime
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import  Blog_Serializer,Category_Serializer,Tag_Serializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def check_api(request):
    resp = {
        "api_name":"drf-api",
        'version':"0.01",
        'status':"good",
        'country':'Nepal',
        }
    return JsonResponse(resp)

@csrf_exempt
def blog_list(request):
    if request.method=='GET':
        blogs = Blog.objects.all()
        serializer = Blog_Serializer(blogs,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif  request.method=='POST':
        data = JSONParser().parse(request)
        serializer = Blog_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        else:
            return JsonResponse(serializer.errors,status = 400)

@csrf_exempt
def single_blog(request,pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = Blog_Serializer(blog)
        return JsonResponse(serializer.data,safe=False)
    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = Blog_Serializer(blog,data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=401)
        else:
            return JsonResponse(serializer.errors,status=400)
    elif request.method =='DELETE':
        blog.delete()
        return JsonResponse(status = 410)


        


