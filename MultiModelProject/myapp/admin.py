from django.contrib import admin
from myapp.models import Department, Employee

# admin.site.register(Department)
# admin.site.register(Employee)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','salary')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('-salary',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    list_filter = ('name',)
    search_fields = ('location',)