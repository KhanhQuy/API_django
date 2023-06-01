from django.urls import path, include
from .views import CompanyListView

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
]