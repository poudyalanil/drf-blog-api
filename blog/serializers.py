from rest_framework import serializers
from .models import Blog,Tag,Category

class Tag_Serializer(serializers.ModelSerializer):
    pass

class Category_Serializer(serializers.ModelSerializer):
    pass

class Blog_Serializer(serializers.ModelSerializer):
    pass

