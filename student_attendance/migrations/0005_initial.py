# Generated by Django 4.1.7 on 2023-03-21 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0007_rename_student_class_name_studentclass_student_class_and_more'),
        ('student_attendance', '0004_delete_studentattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('date', models.DateField()),
                ('student_class', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.studentclass')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentinfo')),
            ],
        ),
    ]
