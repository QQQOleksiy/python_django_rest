from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.serializers import ValidationError

from .models import CarModel


def car_filter_queryset(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()

    for k, v in query.items():
        match k:
            case 'price_gte':
                qs = qs.filter(price__gte=v)
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lte':
                qs = qs.filter(price__lte=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)

            case 'year_gte':
                qs = qs.filter(year__gte=v)
            case 'year_gt':
                qs = qs.filter(year__gt=v)
            case 'year_lte':
                qs = qs.filter(year__lte=v)
            case 'year_lt':
                qs = qs.filter(year__lt=v)

            case 'brand_start':
                qs = qs.filter(brand__istartswith=v)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=v)
            case 'brand_in':
                qs = qs.filter(brand__icontains=v)
            case _:
                raise ValidationError({'detail': f'"{k}" not allowed here'})

    return qs
