from rest_framework.serializers import ModelSerializer
from .models import Company, CompanyUser


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "id",
            "company_name",
            "company_description",
            "address_line1",
            "address_line2",
            "adress_line3",
            "mobile_no1",
            "mobile_no2",
            "email",
            "is_active",
            "created_date",
            "created_by",
            "update_date",
            "update_by",
        ]


class CompanyUserSerializer(ModelSerializer):
    class Meta:
        model = CompanyUser
        fields = [
            "id",
            "company_id",
            "user_id",
            "created_date",
            "created_by",
            "update_date",
            "update_by",
        ]
