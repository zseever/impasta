# Generated by Django 4.1 on 2022-08-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=250)),
                ('phone', models.CharField(max_length=20)),
                ('cuisine', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=1000)),
                ('img', models.CharField(max_length=250)),
            ],
        ),
    ]
