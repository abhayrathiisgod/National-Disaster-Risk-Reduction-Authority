from pressnotenews.models import NewsInfo, PressNote
from django_filters import rest_framework as drf_filters
from pressnotenews.models import Type, Author


class YearFilter(drf_filters.Filter):
    def filter(self, qs, value):
        if value:
            return qs.filter(date__year=value)
        return qs


class NewsInfoFilter(drf_filters.FilterSet):
    date = YearFilter(label='date (year)')
    order_by_id = drf_filters.OrderingFilter(
        fields=(
            ('id', 'id'),
        ),
        label='Order by ID',
    )

    class Meta:
        model = NewsInfo
        fields = []


class PressNoteFilter(drf_filters.FilterSet):
    date = YearFilter(label='date (year)')
    order_by_id = drf_filters.OrderingFilter(
        fields=(
            ('id', 'id'),
        ),
        label='Order by ID',
    )
    type = drf_filters.ChoiceFilter(
        choices=Type.objects.all().values_list('Type_id', 'name'),
        label='Type',
        method='filter_by_type'
    )
    author = drf_filters.ChoiceFilter(
        choices=Author.objects.all().values_list('Author_id', 'name'),
        label='Author',
        method='filter_by_author'
    )

    class Meta:
        model = PressNote
        fields = []

    def filter_by_type(self, queryset, name, value):
        if value:
            return queryset.filter(type=value)
        return queryset

    def filter_by_author(self, queryset, name, value):
        if value:
            return queryset.filter(author=value)
        return queryset
