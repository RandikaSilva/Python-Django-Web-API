from django.urls import path
from .views import CompanyList, CompanyDetails, CompanyUserList, CompanyUserDetails

urlpatterns = [
    path("", CompanyList.as_view()),
    path("<int:id>", CompanyDetails.as_view()),
    path("companyuser/", CompanyUserList.as_view()),
    path("companyuser/<int:id>/", CompanyUserDetails.as_view()),
]
