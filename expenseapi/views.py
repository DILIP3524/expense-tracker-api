from django.shortcuts import render
from rest_framework import generics , viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ExpenseModel , User
from .serializers import RegisterSerializer, ExpenseSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated
from .permissions import IsOwner
from .filtters import ExpenseFilter 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from rest_framework.pagination import PageNumberPagination
from .paginations  import PagesizePagination
# Create your views here.


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer



class ExpenseView(viewsets.ModelViewSet):
    queryset = ExpenseModel.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    filterset_class = ExpenseFilter
    filter_backends = [DjangoFilterBackend , OrderingFilter]
    ordering_fields = ['date_of_expense', 'amount']
    pagination_class = PagesizePagination
    

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user = self.request.user)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



class MonthlyReportView(generics.GenericAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    
    def get(self , request , *args , **kwargs):
        queryset = ExpenseModel.objects.filter(user = request.user)
        summary = (queryset.annotate(month = TruncMonth("date_of_expense")).values("month" , "category").annotate(total = Sum("amount")).order_by("-month" , "category"))

        data = []
        for row in summary:
            data.append({
                "month":row["month"].strftime("%Y-%m"),
                "category": row["category"],
                "total": str(row["total"])
            })

        return Response(data={'results' : data} , status=status.HTTP_200_OK)    




   






