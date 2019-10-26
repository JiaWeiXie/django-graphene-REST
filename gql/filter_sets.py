from django_filters import FilterSet

from .helpers import json_underscoreize, camel_to_underscore


class UnderScoreizeFilterSet(FilterSet):

    def __init__(self, data=None, queryset=None, request=None, prefix=None):
        if data and data.get('order_by'):
            orderings = data['order_by'].strip().split(',')
            data['order_by'] = ','.join(
                [camel_to_underscore(name, **json_underscoreize) for name in orderings]
            )

        super().__init__(data=data, queryset=queryset, request=request, prefix=prefix)
