import django_filters
from .models import ExpenseModel


class ExpenseFilter(django_filters.FilterSet):
    startdate = django_filters.DateFilter(field_name='date_of_expense' , lookup_expr="gte")
    enddate = django_filters.DateFilter(field_name='date_of_expense' , lookup_expr="lte")
    minamount = django_filters.NumberFilter(field_name='amount' , lookup_expr="gte")
    maxamount = django_filters.NumberFilter(field_name='amount' , lookup_expr="lte")
    category = django_filters.CharFilter(field_name="category" , lookup_expr='iexact')

    class Meta:
        model = ExpenseModel
        fields  = ["startdate" , "enddate" , "category" , "minamount" , "maxamount" ]

