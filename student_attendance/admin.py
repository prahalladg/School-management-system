from django.contrib import admin
from .models import StudentAttendance,AttendanceDetails
# Register your models here.
admin.site.register(StudentAttendance)
admin.site.register(AttendanceDetails)