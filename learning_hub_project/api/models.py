from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class LearningHub(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='learning_hubs')

class Course(models.Model):
    name = models.CharField(max_length=255)
    learning_hub = models.ForeignKey(LearningHub, on_delete=models.CASCADE, related_name='courses')
