from rest_framework import serializers

from apps.billing.models import Student, Transactions, Payment


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

        fields = [
            "id",
            "user",
            "first_name",
            "middle_name",
            "last_name",

        ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment

        fields = [
            "id",
            "trans_id",
            "gepg_pay_status",
            "channel",
            "index_number",

        ]


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions

        fields = [
            "id",
            "semester",
            "control_number",
            "trans_date",
            "user",
            "gepg_ack",
            "index_number",
            "payment_status",


        ]
