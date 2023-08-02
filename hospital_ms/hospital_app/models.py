from django.db import models
from django.contrib.auth.models import AbstractUser
from department_doctors_app.models import Doctors


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
    )

    user_type = models.CharField(max_length=100,choices=USER_TYPE_CHOICES, default='user')
    patient_name = models.CharField(max_length=100, blank=False, null=False)
    patient_place = models.CharField(max_length=100, blank=False, null=False)
    patient_phone = models.CharField(max_length=100, blank=False, null=False)
    patient_email = models.EmailField(max_length=255, blank=False)
    patient_password = models.CharField(max_length=128, verbose_name='password', blank=True, null=True)
    patient_department = models.CharField(max_length=200, choices=[('ortho', 'orthopedics'), ('cardio', 'Cardiology'),
                                                                   ('derma', 'Dermatology'), ('Gynec', 'Gynecology'), ])
    admin_name= models.CharField(max_length=100, blank=False, null=False)
    admin_email= models.EmailField(max_length=255, blank=False)
    admin_password= models.CharField(max_length=128, verbose_name='password', blank=True, null=True)


    def __str__(self):
        return self.user_type


class UserAccess(models.Model):
    user = models.OneToOneField(CustomUser, related_name='access', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.user)

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100, unique=True,blank=False, null=False)
    patient_place = models.CharField(max_length=100, blank=False, null=False)
    patient_phone = models.CharField(max_length=100, blank=False, null=False)
    patient_email = models.EmailField(max_length=255, blank=False)
    appointment_date= models.DateTimeField()
    appointment_time= models.ForeignKey('TimeSlot',on_delete=models.CASCADE,unique_for_date='appointment_date')
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)

    patient_department= models.CharField(max_length=200,choices=[ ('ortho', 'orthopedics'), ('cardio', 'Cardiology'),
                                             ('derma', 'Dermatology'),('Gynec','Gynecology'),])
    status=models.CharField(max_length=50,choices=[('confirmed', 'Confirmed'), ('pending', 'Pending'),('rejected','Rejected')])
    history = models.ManyToManyField('History', blank=True,related_name='appointments')
    def __str__(self):
        return self.patient_name


class History(models.Model):
    date = models.DateField()
    time = models.TimeField()
    admin = models.CharField(max_length=255)
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE,related_name='history_entries')

    def __str__(self):
        return self.admin


class TimeSlot(models.Model):

    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f" ({self.start_time} - {self.end_time})"
