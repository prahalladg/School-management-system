# Generated by Django 4.1.7 on 2023-03-10 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_class', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='address',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='dob',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='father_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='gender',
            field=models.CharField(choices=[('1', 'male'), ('2', 'female'), ('3', 'other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='mother_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='student_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='student_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentclass'),
        ),
    ]
