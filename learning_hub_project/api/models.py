from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)

class LearningHub(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, related_name='learning_hubs', on_delete=models.CASCADE)

class Course(models.Model):
    name = models.CharField(max_length=200)
    learning_hub = models.ForeignKey(LearningHub, related_name='courses', on_delete=models.CASCADE)

