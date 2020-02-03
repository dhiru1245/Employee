from django.contrib import admin
from eapp1.models import Employee
from .models import Employee
# Register your models here.

# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['eno','ename','pan_no','age','gender','email','city_name']
admin.site.register(Employee)