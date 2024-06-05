from django.contrib import admin

from department.models import Department, Position


class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


class PositionAdmin(admin.ModelAdmin):
	list_display = ('name', 'department')
	search_fields = ('name', 'department__name')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Position, PositionAdmin)
