# Generated by Django 5.0.6 on 2024-06-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_rename_employee_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='city',
            field=models.CharField(choices=[('DUB', 'Dublin'), ('CORK', 'Cork')], default='Dublin', max_length=50),
        ),
        migrations.AddField(
            model_name='employees',
            name='employment_type',
            field=models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-Time')], default='Full-Time', max_length=50),
        ),
    ]
