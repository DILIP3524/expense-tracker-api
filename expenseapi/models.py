from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)


class ExpenseModel(models.Model):
    CATEGORY_CHOICES = [
        ("food", "Food"),
        ("travel", "Travel"),
        ("shopping", "Shopping"),
        ("bills", "Bills"),
        ("health", "Health"),
        ("other", "Other"),
]
                   

    description = models.TextField(null=False)
    amount = models.DecimalField(max_digits=10 ,decimal_places=2)
    category = models.CharField(max_length=50 ,choices=CATEGORY_CHOICES)
    date_of_expense = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='expenses')
    


