from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100,unique=True, blank=False, null=False,choices=[ ('ortho', 'orthopedics'), ('cardio', 'Cardiology'),
                                             ('derma', 'Dermatology'),('Gynec','Gynecology'),])
    department_description= models.TextField()
    def __str__(self):
        return self.department_name


class Doctors(models.Model):
    doctor_name=models.CharField(max_length=100, unique=True, blank=False, null=False)
    doctor_department_fk = models.ForeignKey(Department, on_delete=models.CASCADE)
    qualification= models.CharField(max_length=50, unique=True, blank=False, null=False)
    photo= models.ImageField(upload_to='photos', max_length=1000)
    def __str__(self):
        return self.doctor_name