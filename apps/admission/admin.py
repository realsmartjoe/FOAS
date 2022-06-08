from django.contrib import admin

# Register your models here.
from apps.admission.models import Payment, Application, EduVerification, EduCategory

admin.site.register(Payment)
admin.site.register(Application)
admin.site.register(EduVerification)
admin.site.register(EduCategory)

