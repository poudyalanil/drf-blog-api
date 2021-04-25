from rest_framework import serializers
from .models import Blog,Tag,Category

class Tag_Serializer(serializers.Serializer):
    tag = serializers.CharField(max_length=255,default=None,blank=False,verbose_name="Tag Name")
    date_created = serializers.DateTimeField(auto_now=True)
    creator = serializers.CharField(max_length=255,default=None,blank=False,verbose_name="Creator")

    def create(self,validated_data):
        return Tag.objects.create(validated_data) 

    def update(self, instance, validated_data):
        instance.tag = validated_data.get('tag',instance.tag)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.creator = validated_data.get('creator',instance.creator)
        instance.save()

        return instance


class Category_Serializer(serializers.ModelSerializer):
    pass

class Blog_Serializer(serializers.ModelSerializer):
    pass

