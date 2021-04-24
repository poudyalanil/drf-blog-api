from rest_framework import serializers
from .models import Blog,Tag,Category

class Tag_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

