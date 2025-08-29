from django.urls import path
from .views import RegisterView , ExpenseView , MonthlyReportView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('register/' , RegisterView.as_view() , name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('summary/monthly/' , MonthlyReportView.as_view() , name = 'montly_report'),

  
]

router = DefaultRouter()
router.register('expenses' ,ExpenseView, )
urlpatterns += router.urls