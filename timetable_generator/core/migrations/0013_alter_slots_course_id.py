# Generated by Django 4.1.4 on 2023-07-09 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_timetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slots',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.course'),
        ),
    ]