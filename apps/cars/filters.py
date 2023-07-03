from django_filters import rest_framework as filters

from apps.cars.choices.body_type_choices import BodyTypeChoices
from apps.cars.models import CarModel


class CarFilter(filters.FilterSet):

    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'body', 'price', 'year')

    year_lt = filters.NumberFilter('year', 'lt')
    year_gt = filters.NumberFilter('year', 'gt')
    year_lte = filters.NumberFilter('year', 'lte')
    year_gte = filters.NumberFilter('year', 'gte')
    year_range = filters.RangeFilter('year')

    price_lt = filters.NumberFilter('price', 'lt')
    price_gt = filters.NumberFilter('price', 'gt')
    price_lte = filters.NumberFilter('price', 'lte')
    price_gte = filters.NumberFilter('price', 'gte')
    price_range = filters.RangeFilter('price')

    brand_contains = filters.CharFilter('brand', 'icontains')
    brand_startswith = filters.CharFilter('brand', 'istartswith')
    brand_endswith = filters.CharFilter('brand', 'iendswith')

    body = filters.ChoiceFilter('body', choices=BodyTypeChoices.choices)

    order = filters.OrderingFilter(
        fields=('id', 'brand', 'body', 'price', 'year')
    )

