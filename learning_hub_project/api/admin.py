from api.models import Company, LearningHub, Course

company = Company.objects.create(name='Company A')
learning_hub = LearningHub.objects.create(name='Hub A', company=company)
course = Course.objects.create(name='Course A', learning_hub=learning_hub)