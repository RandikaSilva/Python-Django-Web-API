from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "product_name",
            "product_desciption",
            "is_active",
            "created_date",
            "created_by",
        ]
