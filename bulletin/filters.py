import django_filters
from .models import Bulletin


class BulletinFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name='date', lookup_expr='year')
    title = django_filters.CharFilter(
        field_name='title', lookup_expr='icontains', label='Title English')
    title_nepali = django_filters.CharFilter(
        field_name='title_ne', lookup_expr='icontains', label='Title Nepali')
    order_by = django_filters.OrderingFilter(
        fields=(
            ('date', 'date'),
        ),
        field_labels={
            'date': 'Date',
        },
    )

    class Meta:
        model = Bulletin
        fields = ['bulletin_type']
