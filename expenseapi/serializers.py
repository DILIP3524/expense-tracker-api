from rest_framework import serializers
from .models import User , ExpenseModel
from django.db import transaction

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    name = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ("email", "password", "name")


    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already registered")
        return value


    @transaction.atomic
    def create(self, validated_data):
        email = validated_data["email"].lower()
        name = validated_data.pop("name")
        user = User(username=email, email=email, first_name=name)
        user.set_password(validated_data["password"]) 
        user.save()
        return user
    

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseModel
        fields = ('user' , 'description' , 'amount' , 'category' , 'date_of_expense' , 'created_at')
        read_only_fields = ('id' , 'user' , 'created_at')


    def validate_amount(self , value):
        if value <=0 : 
            raise serializers.ValidationError("Amount Should be greater than zero")
        return value 

