from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.billing.views import StudentViewSet, TransactionsViewSet, PaymentViewSet

router = DefaultRouter()
router.register('student', StudentViewSet, basename="student")
router.register('transaction', TransactionsViewSet, basename="transaction")
router.register('payment', PaymentViewSet, basename="payment")

urlpatterns = [
    path('', include(router.urls)),
]
