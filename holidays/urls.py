from django.urls import path

from holidays.views import NewHolidayCreateView, HolidayListView, HolidayUpdateView, HolidayDeleteView

urlpatterns = [
	path('new_holiday/', NewHolidayCreateView.as_view(), name='new_holiday'),
	path('holiday_list/', HolidayListView.as_view(), name='holiday_list'),
	path('holiday_update/<int:pk>/', HolidayUpdateView.as_view(), name='holiday_update'),
	path('holiday_delete/<int:pk>/', HolidayDeleteView.as_view(), name='holiday_delete'),

]
