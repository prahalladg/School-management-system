# Generated by Django 4.1.7 on 2023-03-20 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_rename_student_class_name_studentclass_student_class_and_more'),
        ('student_attendance', '0002_rename_studentattendance_studentattendancedetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentAttendanceDetails',
            new_name='StudentAttendance',
        ),
    ]
