from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=20)
    department_code = models.CharField(max_length=3,unique=True)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


