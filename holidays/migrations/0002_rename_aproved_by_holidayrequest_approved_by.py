# Generated by Django 5.0.6 on 2024-06-04 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='holidayrequest',
            old_name='aproved_by',
            new_name='approved_by',
        ),
    ]