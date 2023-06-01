from django.test import TestCase
from api.models import Company, LearningHub, Course
from api.serializers import CompanySerializer, LearningHubSerializer, CourseSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ModelTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Company A")
        self.learning_hub = LearningHub.objects.create(name="Hub A", company=self.company)
        self.course = Course.objects.create(name="Course A", learning_hub=self.learning_hub)

    def test_model_creation(self):
        self.assertEqual(self.company.name, "Company A")
        self.assertEqual(self.learning_hub.name, "Hub A")
        self.assertEqual(self.course.name, "Course A")

class SerializerTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Company A")
        self.learning_hub = LearningHub.objects.create(name="Hub A", company=self.company)
        self.course = Course.objects.create(name="Course A", learning_hub=self.learning_hub)

    def test_serializers(self):
        company_serializer = CompanySerializer(self.company)
        self.assertEqual(company_serializer.data, {'name': 'Company A', 'learning_hubs': [{'name': 'Hub A', 'courses': [{'name': 'Course A'}]}]})

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.company = Company.objects.create(name="Company A")
        self.learning_hub = LearningHub.objects.create(name="Hub A", company=self.company)
        self.course = Course.objects.create(name="Course A", learning_hub=self.learning_hub)

    def test_api_can_get_a_company(self):
        response = self.client.get(reverse('company-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
