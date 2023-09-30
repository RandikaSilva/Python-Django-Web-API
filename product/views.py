from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions


class ProductList(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)


class ProductDetailView(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Product.objects.filter(created_by=self.request.user)
