from django.contrib import admin
from .models import Employee,Department

class DepartmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["department_code"]}),
        (None, {"fields":["department_name"]}),
    ]
class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {"fields":["first_name",'last_name']}),
        ("Personal Details", {"fields":["date_of_birth","salary","department"]}),
        ("Contact", {"fields":["email","phone_number"]}),
    ]

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)
