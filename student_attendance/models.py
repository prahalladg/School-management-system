from django.db import models
from student.models import StudentClass,StudentInfo
# Create your models here.


# Create your models here.
'''model student attendance class'''
class StudentAttendance(models.Model):
    student_class=models.ForeignKey(StudentClass,on_delete=models.CASCADE,default=1)
    

    def __str__(self):
        return str(self.student_class)
    
'''model for attendance details'''
class AttendanceDetails(models.Model):
    date=models.DateField()
    Class=models.ForeignKey(StudentClass,on_delete=models.CASCADE)
    name=models.ForeignKey(StudentInfo,on_delete=models.CASCADE)
    attendance_choice=("Present","Present"),("Absent","Absent")
    attendance=models.CharField(max_length=10,choices=attendance_choice)

    def __str__(self):
        return str(self.name)