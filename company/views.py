from datetime import datetime
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Company
from rest_framework import permissions
from .serializers import CompanySerializer, CompanyUserSerializer
from rest_framework.response import Response
from rest_framework import status


class CompanyList(ListCreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user.id)


class CompanyDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
    queryset = Company.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data["created_by"] = request.user.id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            serializer.validated_data["update_by"] = request.user.id
            serializer.validated_data["update_date"] = datetime.now()
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class CompanyUserList(ListCreateAPIView):
    serializer_class = CompanyUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user.id)

    def get_queryset(self):
        return Company.objects.filter(created_by=self.request.user.id)


class CompanyUserDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = CompanyUserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"
    queryset = Company.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data["created_by"] = request.user.id
            serializer.validated_data["created_date"] = datetime.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            serializer.validated_data["update_by"] = request.user.id
            serializer.validated_data["update_date"] = datetime.now()
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
