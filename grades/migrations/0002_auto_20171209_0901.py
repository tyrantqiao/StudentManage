# Generated by Django 2.0 on 2017-12-09 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grdes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='grade',
            name='student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_class',
            new_name='class_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.AddField(
            model_name='grdes',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.Semester'),
        ),
        migrations.AddField(
            model_name='grdes',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grades.Student'),
        ),
    ]
