from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser

from apps.profiles.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    four_index = models.CharField(default='', max_length=30, null=True)
    is_student = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_applicant = models.BooleanField(default=False)
    form_submitted = models.BooleanField(default=False)
    campus = models.ForeignKey('admission.Campus', blank=True, null=True, related_name='user_campus_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True,
                                default=None)
    dob = models.CharField(default='', max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(default='', max_length=30, null=True, blank=True)
    citizenship = models.CharField(default='', max_length=30, null=True, blank=True)
    middle_name = models.CharField(default='', max_length=30, null=True, blank=True)
    first_name = models.CharField(default='', max_length=30, null=True, blank=True)
    last_name = models.CharField(default='', max_length=30, null=True, blank=True)
    disability = models.CharField(default='', max_length=30, null=True, blank=True)
    phone = models.CharField(default='', max_length=30, null=True, blank=True)
    address = models.CharField(default='', max_length=50, null=True, blank=True)
    postal_address = models.CharField(default='', max_length=50, null=True, blank=True)
    marital_status = models.CharField(default='', max_length=30, null=True, blank=True)
    country = models.CharField(default='', max_length=50, null=True, blank=True)
    region = models.CharField(default='', max_length=50, null=True, blank=True)
    district = models.CharField(default='', max_length=50, null=True, blank=True)
    kin_first_name = models.CharField(default='', max_length=50, null=True, blank=True)
    kin_full_name = models.CharField(default='', max_length=50, null=True, blank=True)
    kin_address = models.CharField(default='', max_length=50, null=True, blank=True)
    kin_phone = models.CharField(default='', max_length=50, null=True, blank=True)
    kin_relationship = models.CharField(default='', max_length=50, null=True, blank=True)
    kin_email = models.CharField(default='', max_length=50, null=True, blank=True)
    kin_region = models.CharField(default='', max_length=50, null=True, blank=True)
