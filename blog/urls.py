from django.urls import path
from . import views

urlpatterns = [
    path('api-check',views.check_api,name="api_check"),
    path('',views.blog_list,name="blog-list")
]