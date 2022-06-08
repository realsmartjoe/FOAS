from django.contrib import admin

# Register your models here.
from apps.profiles.models import User

admin.site.register(User)