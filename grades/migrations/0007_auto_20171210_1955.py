# Generated by Django 2.0 on 2017-12-10 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0006_auto_20171210_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
