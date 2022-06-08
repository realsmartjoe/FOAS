from django.db import models

from apps.profiles.models import User


class Student(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, related_name='s_user_id',
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)


class Transactions(models.Model):
    semester = models.CharField(max_length=200, blank=True, null=True)
    control_number = models.CharField(max_length=200, blank=True, null=True)
    trans_date = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, related_name='transaction',
                             on_delete=models.CASCADE)
    gepg_ack = models.CharField(max_length=50, blank=True, null=True)
    index_number = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=50, blank=True, null=True)


class Payment(models.Model):
    trans_id = models.ForeignKey(Transactions, blank=True, null=True, related_name='payment_trans',
                                 on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, related_name='payment',
                             on_delete=models.CASCADE)
    gepg_pay_status = models.CharField(max_length=200, blank=True, null=True)
    channel = models.CharField(max_length=50, blank=True, null=True)
    index_number = models.CharField(max_length=50, blank=True, null=True)
