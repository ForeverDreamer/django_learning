from rest_framework import pagination


class CFEAPIPagination(pagination.LimitOffsetPagination):  # PageNumberPagination
    # page_size = 3
    default_limit = 3
    max_limit = 10
    limit_query_param = 'lim'
