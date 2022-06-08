from django.conf.urls import url
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import EduCategoryViewSet, EduVerificationViewSet, ApplicationViewSet, ProgrammeViewSet, \
    CampusViewSet
from ..profiles import views
from ..profiles.views import UserViewSet, ProfileViewSet, UpdateUserViewSet, UpdateUserOnlyViewSet, RegisterViewSet

router = DefaultRouter()
router.register('category', EduCategoryViewSet, basename="edu_category")
router.register('verification', EduVerificationViewSet, basename="edu_verification")
router.register('application', ApplicationViewSet, basename="application")
router.register('programme', ProgrammeViewSet, basename="programme")
router.register('campus', CampusViewSet, basename="campus")
router.register(r'profile', UserViewSet, basename="profile")
router.register(r'register', RegisterViewSet, basename="register")
router.register(r'profile_list', ProfileViewSet, basename="profile_list")
router.register(r'update_user', UpdateUserViewSet, basename="update_user")
router.register(r'update_user_only', UpdateUserOnlyViewSet, basename="update_user_only")

urlpatterns = [
    path('', include(router.urls)),
]
