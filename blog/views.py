from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Category, Blog, Tag
from datetime import  datetime
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import  Blog_Serializer,Category_Serializer,Tag_Serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from rest_framework import  status

# Create your views here.
def check_api(request):
    resp = {
        "api_name":"drf-api",
        'version':"0.01",
        'status':"good",
        'country':'Nepal',
        }
    return JsonResponse(resp)

@api_view(['GET','POST'])
def blog_list(request):
    if request.method=='GET':
        blogs = Blog.objects.all()
        serializer = Blog_Serializer(blogs,many=True)
        return Response(serializer.data)
    elif  request.method=='POST':
        serializer = Blog_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def single_blog(request,pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Blog_Serializer(blog)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = Blog_Serializer(blog,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        blog.delete()
        return HttpResponse(status = status.HTTP_410_GONE)


        


