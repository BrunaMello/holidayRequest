from django.contrib import admin

from holidays.models import HolidayRequest


class HolidayRequestAdmin(admin.ModelAdmin):
	list_display = ('employee', 'start_date', 'end_date', 'approved', 'approved_by')
	search_fields = ('employee', 'start_date', 'end_date', 'approved', 'approved_by')


admin.site.register(HolidayRequest, HolidayRequestAdmin)
