from rest_framework.pagination  import PageNumberPagination

class PagesizePagination(PageNumberPagination):
    page_size = 10
    