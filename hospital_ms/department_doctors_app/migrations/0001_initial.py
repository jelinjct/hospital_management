# Generated by Django 4.2.3 on 2023-08-02 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(choices=[('ortho', 'orthopedics'), ('cardio', 'Cardiology'), ('derma', 'Dermatology'), ('Gynec', 'Gynecology')], max_length=100, unique=True)),
                ('department_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100, unique=True)),
                ('qualification', models.CharField(max_length=50, unique=True)),
                ('photo', models.ImageField(max_length=1000, upload_to='photos')),
                ('doctor_department_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department_doctors_app.department')),
            ],
        ),
    ]
