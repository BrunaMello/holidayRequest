from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from employee.forms import NewEmployeeModelForm, UpdateEmployeeModelForm
from employee.models import Employees


class NewEmployeeCreateView(CreateView):
	model = Employees
	template_name = 'new_employee.html'
	form_class = NewEmployeeModelForm
	success_url = '/employee/employee_list/'


class EmployeeListView(ListView):
	model = Employees
	template_name = 'employee_list.html'
	context_object_name = 'employees'

	def get_queryset(self):
		employees = super().get_queryset().order_by('id')
		search = self.request.GET.get('search')
		if search:
			employees = employees.filter(name__icontains=search)
		return employees


class EmployeeDetailView(ListView):
	model = Employees
	template_name = 'employee_detail.html'
	context_object_name = 'employees'

	def get_queryset(self):
		employees = super().get_queryset().order_by('id')
		search = self.request.GET.get('search')
		if search:
			employees = employees.filter(name__icontains=search)
		return employees


class EmployeeUpdateView(UpdateView):
	model = Employees
	template_name = 'employee_update.html'
	form_class = UpdateEmployeeModelForm
	success_url = '/employee/employee_list/'


class EmployeeDeleteView(DeleteView):
	model = Employees
	template_name = 'employee_delete.html'
	success_url = '/employee/employee_list/'
