from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from holidays.forms import NewHolidayModelForm, UpdateHolidayModelForm
from holidays.models import HolidayRequest


class NewHolidayCreateView(CreateView):
	model = HolidayRequest
	template_name = 'new_holiday.html'
	form_class = NewHolidayModelForm
	success_url = '/holidays/holiday_list/'


class HolidayListView(ListView):
	model = HolidayRequest
	template_name = 'holiday_list.html'
	context_object_name = 'holidays'

	def get_queryset(self):
		holidays = super().get_queryset().order_by('start_date')
		search = self.request.GET.get('search')
		if search:
			holidays = holidays.filter(name__icontains=search)
		return holidays


class HolidayUpdateView(UpdateView):
	model = HolidayRequest
	form_class = UpdateHolidayModelForm
	template_name = 'holiday_update.html'
	success_url = '/holidays/holiday_list/'


class HolidayDeleteView(DeleteView):
	model = HolidayRequest
	template_name = 'holiday_delete.html'
	success_url = '/holidays/holiday_list/'
