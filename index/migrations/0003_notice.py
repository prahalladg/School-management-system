# Generated by Django 4.1.7 on 2023-03-16 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=200)),
            ],
        ),
    ]