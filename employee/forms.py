from django import forms

from employee.models import Employees


class NewEmployeeModelForm(forms.ModelForm):
	class Meta:
		model = Employees
		fields = (
			'name', 'email', 'department', 'position', 'city', 'employment_type', 'hire_date', 'is_active')
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'department': forms.Select(attrs={'class': 'form-control'}),
			'position': forms.Select(attrs={'class': 'form-control'}),
			'city': forms.Select(attrs={'class': 'form-control'}),
			'employment_type': forms.Select(attrs={'class': 'form-control'}),
			'hire_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
			'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
		}


class UpdateEmployeeModelForm(forms.ModelForm):
	class Meta:
		model = Employees
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'department': forms.Select(attrs={'class': 'form-control'}),
			'position': forms.Select(attrs={'class': 'form-control'}),
			'city': forms.Select(attrs={'class': 'form-control'}),
			'employment_type': forms.Select(attrs={'class': 'form-control'}),
			'hire_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
			'fire_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
			'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
		}
