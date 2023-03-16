from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from .models import StudentAttendance,AttendanceDetails
from student.models import StudentInfo,StudentClass
# Create your forms here.



class StudentAttendanceForm(forms.ModelForm):
    
    class Meta:
        model = StudentAttendance
        fields = '__all__'
        

class AllAttendanceDetails(forms.Form):
    date=forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model=AttendanceDetails
        fields='__all__'
        include=('date')

