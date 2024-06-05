from datetime import date

from django.db import models

from department.models import Department, Position
from utils import helpers


# Create your models here.

class Employees(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(blank=True, null=True)
	department = models.ForeignKey(Department, on_delete=models.PROTECT)
	position = models.ForeignKey(Position, on_delete=models.PROTECT)
	city = models.CharField(choices=helpers.city, max_length=50, default='Dublin')
	employment_type = models.CharField(choices=helpers.employment_type, max_length=50, default='Full-Time')
	hire_date = models.DateField(default=date.today(), editable=True)
	fire_date = models.DateField(null=True, blank=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
