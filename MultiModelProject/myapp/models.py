from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Department'

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name='employees')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Employee'