# Generated by Django 2.0 on 2017-12-09 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0004_semester_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
    ]
