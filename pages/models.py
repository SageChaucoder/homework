from django.db import models

# Create your models here.

class Member(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField(max_length=100)
    Location = models.CharField(max_length=100)

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Price = models.FloatField(default=0.00)
    Quantity = models.IntegerField()

class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Position = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Salary = models.IntegerField()

