from django.urls import path
from . import views

urlpatterns = [
    path('api-check',views.check_api,name="api_check"),
    path('',views.blog_list,name="blog_list"),
    path('detail/<int:pk>',views.single_blog,name='single_blog')
]