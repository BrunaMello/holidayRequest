from django import forms

from .models import HolidayRequest


class NewHolidayModelForm(forms.ModelForm):
	class Meta:
		model = HolidayRequest
		fields = '__all__'
		widgets = {
			'employee': forms.Select(attrs={'class': 'form-control'}),
			'start_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
			'end_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
			'approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'approved_by': forms.Select(attrs={'class': 'form-control'}),
		}

	def __init__(self, *args, **kwargs):
		super(NewHolidayModelForm, self).__init__(*args, **kwargs)
		self.fields['employee'].queryset = self.fields['employee'].queryset.order_by('name')


class UpdateHolidayModelForm(forms.ModelForm):
	class Meta:
		model = HolidayRequest
		fields = '__all__'
		widgets = {
			'employee': forms.Select(attrs={'class': 'form-control'}),
			'start_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
			'end_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
			'approved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
			'approved_by': forms.Select(attrs={'class': 'form-control'}),
		}

	def __init__(self, *args, **kwargs):
		super(UpdateHolidayModelForm, self).__init__(*args, **kwargs)
		self.fields['employee'].queryset = self.fields['employee'].queryset.order_by('name')
