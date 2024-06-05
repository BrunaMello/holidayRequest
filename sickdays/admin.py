from django.contrib import admin

from sickdays.models import SickDayRequest


class SickDayRequestAdmin(admin.ModelAdmin):
	list_display = ('employee', 'start_date', 'end_date', 'comment', 'approved', 'approved_by')
	search_fields = ('employee', 'start_date', 'end_date', 'approved', 'approved_by')


admin.site.register(SickDayRequest, SickDayRequestAdmin)
