from django.shortcuts import render
from rest_framework import viewsets

from apps.billing.models import Student, Transactions, Payment
from apps.billing.serializers import StudentSerializer, TransactionsSerializer, PaymentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class TransactionsViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionsSerializer
    queryset = Transactions.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
