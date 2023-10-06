from rest_framework import serializers
from task.models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'password',
            'bio',
            'image'            
        ]
        def get_image(self, obj):
            request = self.context.get('request')
            if obj.image:
                image = obj.image.url
                return request.build_absolute_uri(image)
            return None

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'