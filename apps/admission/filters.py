import django_filters

from apps.admission.models import Application
from apps.profiles.models import User


class ApplicationFilter(django_filters.FilterSet):
    user = django_filters.ModelChoiceFilter(field_name="user__slug",
                                            queryset=User.objects.all())

    class Meta:
        model = Application
        fields = ('user',)
