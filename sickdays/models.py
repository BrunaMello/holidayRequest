from django.contrib.auth.models import User
from django.db import models

from employee.models import Employees


class SickDayRequest(models.Model):
	employee = models.ForeignKey(Employees, on_delete=models.PROTECT)
	start_date = models.DateField()
	end_date = models.DateField()
	comment = models.TextField(blank=True, null=True)
	approved = models.BooleanField(default=False)
	approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

	def __str__(self):
		return f'{self.employee} - {self.start_date} to {self.end_date}'
