# Generated by Django 5.1.3 on 2024-12-29 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_streamrequest_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='streamrequest',
            old_name='programName',
            new_name='program_name',
        ),
        migrations.RenameField(
            model_name='streamrequest',
            old_name='startDate',
            new_name='start_date',
        ),
    ]
