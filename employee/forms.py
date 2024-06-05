from django import forms

from employee.models import Employees


class EmployeeModelForm(forms.ModelForm):
	class Meta:
		model = Employees
		fields = '__all__'
