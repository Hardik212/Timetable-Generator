# Generated by Django 4.1.4 on 2023-06-25 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_courseoffered_delete_courseprogram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFaculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.IntegerField()),
                ('faculty_sname', models.CharField(max_length=20)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course')),
            ],
        ),
        migrations.AddConstraint(
            model_name='coursefaculty',
            constraint=models.UniqueConstraint(fields=('course_id', 'section'), name='unique_courseFaculty'),
        ),
    ]