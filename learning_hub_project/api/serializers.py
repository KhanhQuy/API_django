from rest_framework import serializers
from .models import Company, LearningHub, Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']

class LearningHubSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = LearningHub
        fields = ['name', 'courses']

class CompanySerializer(serializers.ModelSerializer):
    learning_hubs = LearningHubSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['name', 'learning_hubs']
