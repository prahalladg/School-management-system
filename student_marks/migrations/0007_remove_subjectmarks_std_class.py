# Generated by Django 4.1.7 on 2023-03-14 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_marks', '0006_alter_subjectmarks_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectmarks',
            name='std_class',
        ),
    ]
