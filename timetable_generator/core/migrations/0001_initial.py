# Generated by Django 4.1.4 on 2023-06-02 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
