import django_filters
from .models import District
from .models import Province


class DistrictFilter(django_filters.FilterSet):
    province = django_filters.ModelChoiceFilter(
        field_name='province', queryset=Province.objects.all())

    class Meta:
        model = District
        fields = ['province']
