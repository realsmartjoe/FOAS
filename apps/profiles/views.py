from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from apps.profiles.models import Profile
from apps.profiles.serializers import UserSerializer, UpdateUserSerializer, ProfileSerializer, UpdateUserOnlySerializer, \
    RegisterSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['get', 'post', 'put'],
            permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        u = User.objects.filter(pk=request.user.pk)[0]
        p = Profile.objects.filter(user=u)[0]
        return Response({"id": u.id, "first_name": u.first_name, "last_name": u.last_name, "email": u.email,
                         "city": p.city, "country": p.country, "bio": p.bio})

    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['get', 'post', 'put'],
            permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        u = User.objects.filter(pk=request.user.pk)[0]
        p = Profile.objects.filter(user=u)[0]
        return Response({"id": u.id, "first_name": u.first_name, "last_name": u.last_name, "email": u.email,
                         "city": p.city, "country": p.country, "bio": p.bio})

    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UpdateUserViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['get', 'post', 'put'],
            permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        u = User.objects.filter(pk=request.user.pk)[0]
        p = Profile.objects.filter(user=u)[0]
        return Response({"id": u.id, "first_name": u.first_name, "last_name": u.last_name, "email": u.email,
                         "city": p.city, "country": p.country, "bio": p.bio})

    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer


class UpdateUserOnlyViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['get', 'post', 'put'],
            permission_classes=[permissions.IsAuthenticated])
    def profile(self, request):
        u = User.objects.filter(pk=request.user.pk)[0]
        p = Profile.objects.filter(user=u)[0]
        return Response({"id": u.id, "first_name": u.first_name, "last_name": u.last_name, "email": u.email,
                         "city": p.city, "country": p.country, "bio": p.bio})

    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UpdateUserOnlySerializer


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
