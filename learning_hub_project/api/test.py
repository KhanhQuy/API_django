from django.test import TestCase
from api.models import Company, LearningHub, Course
from api.serializers import CompanySerializer, LearningHubSerializer, CourseSerializer

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

class ModelTesting(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="Company X")
        self.learning_hub = LearningHub.objects.create(name="Hub X", company=self.company)
        self.course = Course.objects.create(name="Course X", learning_hub=self.learning_hub)

    def test_model_creation(self):
        self.assertEqual(self.company.name, "Company X")
        self.assertEqual(self.learning_hub.name, "Hub X")
        self.assertEqual(self.course.name, "Course X")