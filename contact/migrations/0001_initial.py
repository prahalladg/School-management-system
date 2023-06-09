# Generated by Django 4.1.7 on 2023-03-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='contactlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=900)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]
