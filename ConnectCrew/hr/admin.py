from django.contrib import admin
from hr.models import Employee,Department,Designation
# Register your models here.

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Designation)