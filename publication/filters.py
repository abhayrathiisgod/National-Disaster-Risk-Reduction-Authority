from .models import Publications
from django_filters import rest_framework as filters
from .models import PublicationType, PublicationAuthor


class YearFilter(filters.Filter):
    def filter(self, qs, value):
        if value:
            return qs.filter(date__year=value)
        return qs


class PublicationsFilter(filters.FilterSet):
    pub_type = filters.ChoiceFilter(
        choices=PublicationType.objects.all().values_list('id', 'publication_type'),
        label='Publication Type'
    )
    pub_author = filters.ChoiceFilter(
        choices=PublicationAuthor.objects.all().values_list('id', 'publication_author'),
        label='Publication Author'
    )
    date = YearFilter(field_name='date', label='Date (Year)')
    order_by_id = filters.OrderingFilter(
        fields=(
            ('id', 'id'),
        ),
        label='Order by ID',
    )
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Search'
    )

    class Meta:
        model = Publications
        fields = []
