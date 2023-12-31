# Generated by Django 4.1.4 on 2023-11-08 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_autumn_one_autumn_one_unique_autumn1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winter_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('section', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course')),
                ('faculty_sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.faculty')),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.program')),
            ],
        ),
        migrations.CreateModel(
            name='Autumn_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('section', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course')),
                ('faculty_sname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.faculty')),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.program')),
            ],
        ),
        migrations.AddConstraint(
            model_name='winter_one',
            constraint=models.UniqueConstraint(fields=('course_id', 'program_id', 'year', 'section'), name='unique_winter1'),
        ),
        migrations.AddConstraint(
            model_name='autumn_two',
            constraint=models.UniqueConstraint(fields=('course_id', 'program_id', 'year', 'section'), name='unique_autumn2'),
        ),
    ]
