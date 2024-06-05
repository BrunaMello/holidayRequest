from django.contrib import admin

from employee.models import Employees


class EmployeeAdmin(admin.ModelAdmin):
	list_display = (
		'name', 'email', 'position', 'department', 'hire_date', 'fire_date', 'is_active', 'city', 'employment_type')
	search_fields = ('name',)


admin.site.register(Employees, EmployeeAdmin)
