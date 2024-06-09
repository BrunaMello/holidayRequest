from django.contrib.auth.models import User
from django.db import models

from employee.models import Employees


# Create your models here.

class HolidayRequest(models.Model):
	employee = models.ForeignKey(Employees, on_delete=models.PROTECT)
	start_date = models.DateField()
	end_date = models.DateField()
	approved = models.BooleanField(default=False)
	approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
