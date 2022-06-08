from rest_framework import serializers

from apps.billing.models import Transactions, Payment
from apps.profiles.models import Profile, User
from apps.billing.serializers import TransactionsSerializer, PaymentSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'dob', 'disability', 'first_name', 'last_name', 'middle_name', 'phone', 'gender', 'city', 'citizenship',
            'postal_address', 'marital_status', 'country', 'region', 'district', 'kin_full_name', 'kin_address',
            'kin_phone',
            'kin_relationship', 'kin_email', 'kin_region', 'user')
        read_only_fields = ('user',)


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    transaction = TransactionsSerializer()
    payment = PaymentSerializer()
    campus_name = serializers.CharField(source='campus.campus_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'password', 'campus_name', 'last_name', 'profile', 'is_superuser',
                  'form_submitted', 'four_index', 'transaction', 'payment',
                  'campus', 'is_employee', 'last_login')
        actions_readonly_fields = {
            ('update', 'partial_update'): ('password',)
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        transaction_data = validated_data.pop('transaction')
        payment_data = validated_data.pop('payment')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, **profile_data)
        Transactions.objects.create(user=user, **transaction_data)
        Payment.objects.create(user=user, **payment_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        if profile_data:
            Profile.objects.filter(user_id=self.context['request'].user.id).update(**profile_data)
            Profile.objects.filter(user_id=self.context['request'].user.id).update(form_submitted=True)
            print(self.context['request'].user.id)
        return super().update(instance, validated_data)


class UpdateUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'profile', 'is_superuser', 'is_employee', 'is_student')
        actions_readonly_fields = {
            ('update', 'partial_update'): ('password',)
        }

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        if profile_data:
            Profile.objects.filter(user_id=self.context['request'].user.id).update(**profile_data)
            User.objects.filter(id=self.context['request'].user.id).update(form_submitted=True)
            User.objects.filter(id=self.context['request'].user.id).update(**validated_data)
            print(self.context['request'].user.id)
        return instance


class UpdateUserOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'is_superuser', 'is_employee', 'is_student', 'campus')
        actions_readonly_fields = {
            ('update', 'partial_update'): ('password',)
        }

    def update(self, instance, validated_data):
        print(self.context['request'].user.id)
        return super().update(instance, validated_data)


class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    campus_name = serializers.CharField(source='campus.campus_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'password', 'campus_name', 'last_name', 'profile', 'is_superuser',
                  'form_submitted', 'four_index',
                  'campus', 'is_employee', 'last_login')
        actions_readonly_fields = {
            ('update', 'partial_update'): ('password',)
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        if profile_data:
            Profile.objects.filter(user_id=self.context['request'].user.id).update(**profile_data)
            print(self.context['request'].user.id)
        return super().update(instance, validated_data)
