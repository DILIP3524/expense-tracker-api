from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, ExpenseModel

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'is_staff')

@admin.register(ExpenseModel)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'category', 'date_of_expense', 'created_at')
    list_filter = ('category', 'date_of_expense')