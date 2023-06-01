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

# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Company, LearningHub, Course

# class ModelTestCase(TestCase):
#     """This class defines the test suite for the Company, LearningHub and Course models."""

#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.company_name = "Company A"
#         self.company = Company(name=self.company_name)

#         self.learning_hub_name = "Learning Hub A"
#         self.learning_hub = LearningHub(name=self.learning_hub_name, company=self.company)

#         self.course_name = "Course A"
#         self.course = Course(name=self.course_name, learning_hub=self.learning_hub)

#     def test_models_can_create_a_company_learninghub_and_course(self):
#         """Test the Company, LearningHub and Course model can create a Company, LearningHub, and Course."""
#         old_count_company = Company.objects.count()
#         old_count_learning_hub = LearningHub.objects.count()
#         old_count_course = Course.objects.count()
#         self.company.save()
#         self.learning_hub.save()
#         self.course.save()
#         new_count_company = Company.objects.count()
#         new_count_learning_hub = LearningHub.objects.count()
#         new_count_course = Course.objects.count()
#         self.assertNotEqual(old_count_company, new_count_company)
#         self.assertNotEqual(old_count_learning_hub, new_count_learning_hub)
#         self.assertNotEqual(old_count_course, new_count_course)

# class ViewTestCase(TestCase):
#     """Test suite for the api views."""

#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.client = APIClient()
#         self.company_data = {'name': 'Company B'}
#         self.response = self.client.post(
#             reverse('company-list'),
#             self.company_data,
#             format="json")

#     def test_api_can_create_a_company(self):
#         """Test the api has company creation capability."""
#         self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

#     def test_api_can_get_a_company(self):
#         """Test the api can get a given company."""
#         company = Company.objects.get()
#         response = self.client.get(
#             reverse('company-details', kwargs={'pk': company.id}), format="json")
        
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, company)

#     def test_api_can_update_company(self):
#         """Test the api can update a given company."""
#         company = Company.objects.get()
#         change_company = {'name': 'Company C'}
#         response = self.client.put(
#             reverse('company-details', kwargs={'pk': company.id}),
#             change_company, format='json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_api_can_delete_company(self):
#         """Test the api can delete a company."""
#         company = Company.objects.get()
#         response = self.client.delete(
#             reverse('company-details', kwargs={'pk': company.id}),
#             format='json', follow=True)
#         self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
 