from django.db import models

from apps.profiles.models import User


class Campus(models.Model):
    campus_name = models.CharField(max_length=11, blank=True, null=True)
    location = models.CharField(max_length=11, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='c_created_by_id',
                                   on_delete=models.CASCADE)
    status = models.CharField(max_length=50, blank=True, null=True)


class College(models.Model):
    college_name = models.CharField(max_length=11, blank=True, null=True)
    location = models.CharField(max_length=11, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='coll_created_by_id',
                                   on_delete=models.CASCADE)
    status = models.CharField(max_length=50, blank=True, null=True)


class Programme(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    program_code = models.CharField(max_length=11, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='p_created_by_id',
                                   on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, blank=True, null=True, related_name='p_c_created_by_id',
                               on_delete=models.CASCADE)
    status = models.CharField(max_length=50, blank=True, null=True)


class EduCategory(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='edu_created_by_id',
                                   on_delete=models.CASCADE)
    status = models.CharField(max_length=50, blank=True, null=True)


class EduVerification(models.Model):
    four_results = models.CharField(max_length=50, blank=True, null=True)
    six_results = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)


class Payment(models.Model):
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    amount = models.CharField(max_length=11, blank=True, null=True)
    payment_mode = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    applicant_category = models.ForeignKey(EduCategory, blank=True, null=True, related_name='e_category_id',
                                           on_delete=models.CASCADE)

    status = models.CharField(max_length=50, blank=True, null=True)


class Application(models.Model):
    reference_number = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='applicant', null=True,
                                default=None)
    payment = models.ForeignKey(Payment, blank=True, null=True, related_name='payment_id',
                                on_delete=models.CASCADE)
    education = models.ForeignKey(Payment, blank=True, null=True, related_name='education_id',
                                  on_delete=models.CASCADE)
    choice_one = models.CharField(max_length=50, blank=True, null=True)
    choice_two = models.CharField(max_length=50, blank=True, null=True)
    choice_three = models.CharField(max_length=50, blank=True, null=True)
    selected_programme = models.CharField(default='', max_length=50, blank=True, null=True)
    selected_campus = models.CharField(default='', max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True, related_name='app_created_by_id',
                                   on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, blank=True, null=True, related_name='app_c_created_by_id',
                               on_delete=models.CASCADE)
    status = models.CharField(default='pending', max_length=50, blank=True, null=True)
