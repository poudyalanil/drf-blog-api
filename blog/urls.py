from django.urls import path
from . import views

urlpatterns = [
    path('',views.check_api,name="api_check"),
]