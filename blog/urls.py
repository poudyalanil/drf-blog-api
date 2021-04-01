from django.urls import path
from .views import check_api,BlogView,single_blog,check_api


urlpatterns = [
    path('api-check',check_api,name="api_check"),
    path('',BlogView.as_view(),name="all_blogs"),
    path('detail/<int:pk>',single_blog,name='single_blog')
]