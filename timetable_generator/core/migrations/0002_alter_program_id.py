# Generated by Django 4.1.4 on 2023-06-02 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.CharField(max_length=2, primary_key=True, serialize=False),
        ),
    ]