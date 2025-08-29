from django.test import TestCase
from django.urls import reverse
from .models import User , ExpenseModel
from rest_framework import test
from rest_framework import status

# Create your tests here.


class ExpenseAPITest(test.APITestCase):

    def setUp(self):
     
        self.user = User.objects.create_user(
            first_name="sanjeet",
            email="sanjeet@example.com",
            username = "sanjeet@example.com",
            password="12345678"
        )

   
        self.register_url = reverse("register")
        self.login_url = reverse("token_obtain_pair")  
        self.expense_list_url = reverse("expensemodel-list")  

        self.expense_data = {
            "amount": 250,
            "category": "food",
            "description": "Lunch with colleagues",
            "date_of_expense": "2025-08-29"
        }

    def test_user_registration(self):
        """Test that a new user can register"""
        data = {
            "email": "newuser@example.com",
            "password": "strongpass123",
            "name": "New User"
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="newuser@example.com").exists())

    def test_unauthorized_expense_creation(self):
        """Test that unauthenticated users cannot create expenses"""
        response = self.client.post(self.expense_list_url, self.expense_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_expense_creation_authenticated(self):
        """Test that logged-in user can create expense"""
        
        response = self.client.post(self.login_url, {
            "username": "sanjeet@example.com",
            "password": "12345678"
        }, format="json")
        # print(response.data)
        token = response.data["access"]

      
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

        response = self.client.post(self.expense_list_url, self.expense_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["category"], "food")
        self.assertTrue(ExpenseModel.objects.filter(user=self.user, category="food").exists())