from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import AllAttendanceDetails
from .models import AttendanceDetails


def addAttendance(request):
	'''Here we add addtendance to student and display the attendance details'''
	
	if request.method == "POST":
		attendance_details=AllAttendanceDetails(request.POST)
		date=request.POST.get('date')
		name=request.POST.get('name')
		att_data = AttendanceDetails.objects.all()
		print(att_data)
		exist= AttendanceDetails.objects.filter(name=name,date=date).exists()
		print(exist)
		if attendance_details.is_valid():
			attendance_details.save()
		
			return redirect('/studentattendance')
		else:
			print(attendance_details.errors)
	attendance_details=AllAttendanceDetails()
	attendancedata = AttendanceDetails.objects.all().order_by("Class")
	totalpresent=AttendanceDetails.objects.filter()
	print(attendancedata)
	return render(request,'student_attendance/add_attendance.html',context={"addattendance":attendance_details,'attendancedata':attendancedata})