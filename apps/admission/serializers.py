from rest_framework import serializers
from rest_framework.authtoken.admin import User

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from apps.admission.models import EduCategory, EduVerification, Payment, Application, Programme, Campus
from apps.profiles.models import Profile


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'profile')


class EduCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EduCategory
        read_only_fields = (
            "created_at",
            "created_by",
        )
        fields = [
            "id",
            "name",
            "created_at",
            "created_by",
            "status"
        ]


class EduVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduVerification

        fields = [
            "id",
            "four_results",
            "six_results",
            "status"
        ]


class ProgrammeSerializer(serializers.ModelSerializer):
    campus_name = serializers.CharField(source='campus.campus_name', read_only=True)

    class Meta:
        model = Programme

        fields = [
            "id",
            "name",
            "program_code",
            "created_at",
            "created_by",
            "campus_name",
            "campus",
            "status"
        ]


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus

        fields = [
            "id",
            "campus_name",
            "location",
            "created_at",
            "created_by",
            "status"
        ]


def increment_reference_number():
    last_reference_number = Application.objects.all().order_by('id').last()
    if not last_reference_number:
        return 'FETA0AS0001'
    reference_number = last_reference_number.reference_number
    reference_number_int = int(reference_number.split('FETA0AS')[-1])
    width = 8
    new_reference_number_int = reference_number_int + 1
    formatted = (width - len(str(new_reference_number_int))) * "0" + str(new_reference_number_int)
    new_reference_number_no = 'FETA0AS' + str(formatted)
    return new_reference_number_no


class ApplicationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    four_index = serializers.CharField(source='user.profile.four_index', read_only=True)
    reference_number = serializers.CharField(default=increment_reference_number)

    class Meta:
        model = Application

        fields = [
            "id",
            "reference_number",
            "payment",
            "education",
            "choice_one",
            "choice_two",
            "choice_three",
            "created_at",
            "first_name",
            "last_name",
            "four_index",
            "selected_programme",
            "selected_campus",
            "user",
            "status",
            "campus"

        ]

    def update(self, instance, validated_data):
        instance.selected_programme = validated_data.get('selected_programme', instance.selected_programme)
        instance.status = validated_data.get('status', instance.status)
        instance.selected_campus = validated_data.get('selected_campus', instance.selected_campus)
        instance.save()
        return instance
