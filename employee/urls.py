from django.urls import path

from employee.views import NewEmployeeCreateView, EmployeeListView, EmployeeDetailView, EmployeeDeleteView, \
	EmployeeUpdateView

urlpatterns = [
	path('new_employee/', NewEmployeeCreateView.as_view(), name='new_employee'),
	path('employee_list/', EmployeeListView.as_view(), name='employee_list'),
	path('employee_list/<int:pk>/', EmployeeListView.as_view(), name='employee_list'),
	path('employee_detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
	path('employee_update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
	path('employee_delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),

]
