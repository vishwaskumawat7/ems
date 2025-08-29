from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Department, Employee
from datetime import date
from decimal import Decimal


class DepartmentModelTest(TestCase):

    def test_create_department(self):
        dept = Department.objects.create(
            department_name="Human Resources",
            department_code="HR1"
        )
        self.assertEqual(dept.department_name, "Human Resources")
        self.assertEqual(str(dept), "Human Resources")

    def test_department_code_unique(self):
        Department.objects.create(department_name="Finance", department_code="FIN")
        with self.assertRaises(Exception):  
            Department.objects.create(department_name="Accounts", department_code="FIN")


class EmployeeModelTest(TestCase):

    def setUp(self):
        self.dept = Department.objects.create(
            department_name="IT",
            department_code="IT1"
        )

    def test_create_employee(self):
        emp = Employee.objects.create(
            department=self.dept,
            first_name="John",
            last_name="Doe",
            date_of_birth=date(1990, 5, 20),
            email="john.doe@example.com",
            phone_number="1234567890123",
            salary=Decimal("50000.00")
        )
        self.assertEqual(str(emp), "John Doe")
        self.assertEqual(emp.department.department_name, "IT")

    def test_email_unique(self):
        Employee.objects.create(
            department=self.dept,
            first_name="Jane",
            last_name="Doe",
            date_of_birth=date(1992, 7, 15),
            email="jane.doe@example.com",
            phone_number="1234567890123",
            salary=Decimal("60000.00")
        )
        with self.assertRaises(Exception):  
            Employee.objects.create(
                department=self.dept,
                first_name="Janet",
                last_name="Smith",
                date_of_birth=date(1993, 8, 10),
                email="jane.doe@example.com",  
                phone_number="3210987654321",
                salary=Decimal("55000.00")
            )