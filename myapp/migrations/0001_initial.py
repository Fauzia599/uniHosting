# Generated by Django 5.1.4 on 2025-01-24 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone_no', models.CharField(blank=True, max_length=15, null=True)),
                ('Gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10)),
                ('Address', models.CharField(max_length=100)),
                ('Role', models.CharField(choices=[('Admin', 'Admin'), ('Clerner', 'Clerner')], max_length=10)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('Password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=100)),
                ('task_name', models.CharField(max_length=100)),
                ('cleaner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.cleaner')),
            ],
        ),
    ]
