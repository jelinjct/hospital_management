from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from department_doctors_app.models import Doctors



class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, default='user')
    user_access = models.OneToOneField('UserAccess', related_name='useracc', on_delete=models.CASCADE, null=True,
                                       blank=True)
    def __str__(self):
        return self.user_type

User = get_user_model()

class UserAccess(models.Model):
    user = models.OneToOneField(CustomUser, related_name='uaccess', on_delete=models.CASCADE, null=True, blank=True)
    can_edit = models.BooleanField(default=False)
    can_view = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)


class Appointment(models.Model):
    TokenNo = models.AutoField(primary_key=True, unique=True)
    patient_name = models.CharField( max_length=100,blank=False, null=False)
    patient_place = models.CharField(max_length=100, blank=False, null=False)
    patient_phone = models.CharField(max_length=100, blank=False, null=False)
    patient_email = models.EmailField(max_length=255, blank=False)
    appointment_date = models.DateTimeField()
    appointment_time = models.ForeignKey('TimeSlot', on_delete=models.CASCADE, unique_for_date='appointment_date')
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_department = models.CharField(max_length=200, choices=[('ortho', 'orthopedics'), ('cardio', 'Cardiology'),
                                                                   ('derma', 'Dermatology'), ('Gynec', 'Gynecology'), ])
    status = models.CharField(max_length=50, choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'),
                                                      ('rejected', 'Rejected')])
    history = models.ManyToManyField('History', blank=True, related_name='appointments')

    def __str__(self):
        return str(self.TokenNo)


class History(models.Model):
    date = models.DateField()
    time = models.TimeField()
    admin = models.CharField(max_length=255)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='history_entries')

    def __str__(self):
        return self.admin



class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f" ({self.start_time} - {self.end_time})"
