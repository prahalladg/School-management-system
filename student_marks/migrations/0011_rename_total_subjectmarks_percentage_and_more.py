# Generated by Django 4.1.7 on 2023-03-15 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_marks', '0010_subjectmarks_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subjectmarks',
            old_name='Total',
            new_name='percentage',
        ),
        migrations.AddField(
            model_name='subjectmarks',
            name='total',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]