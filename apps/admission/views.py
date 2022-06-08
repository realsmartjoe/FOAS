from django.shortcuts import render
from django_filters.rest_framework import filters, DjangoFilterBackend

from rest_framework import viewsets, permissions

from .filters import ApplicationFilter
from .models import EduCategory, EduVerification, Payment, Application, Programme, Campus
from .serializers import EduCategorySerializer, EduVerificationSerializer, ApplicationSerializer, \
    ProgrammeSerializer, CampusSerializer


class EduCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = EduCategorySerializer
    queryset = EduCategory.objects.all()


class EduVerificationViewSet(viewsets.ModelViewSet):
    serializer_class = EduVerificationSerializer
    queryset = EduVerification.objects.all()




class ProgrammeViewSet(viewsets.ModelViewSet):
    serializer_class = ProgrammeSerializer
    queryset = Programme.objects.all()


class CampusViewSet(viewsets.ModelViewSet):
    serializer_class = CampusSerializer
    queryset = Campus.objects.all()


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)
