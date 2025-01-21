from django.db import models

# Create your models here.

class Member(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField(max_length=100)
    Location = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Price = models.FloatField(default=0.00)
    Quantity = models.IntegerField()

    def __str__(self):
        return self.Name

class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Position = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Salary = models.IntegerField()

    def __str__(self):
        return self.Name

