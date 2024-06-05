from django.db import models


class Department(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Position(models.Model):
	name = models.CharField(max_length=100)
	department = models.ForeignKey('Department', on_delete=models.PROTECT)

	def __str__(self):
		return self.name
