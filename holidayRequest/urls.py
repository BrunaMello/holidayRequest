from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('employee/', include('employee.urls')),
	path('holidays/', include('holidays.urls')),
	path('department/', include('department.urls')),
]
