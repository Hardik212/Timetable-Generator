# Generated by Django 4.1.4 on 2023-06-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_program_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=80)),
                ('course_credits', models.CharField(max_length=15)),
            ],
        ),
    ]
