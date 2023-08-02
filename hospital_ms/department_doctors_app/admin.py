from django.contrib import admin
from department_doctors_app.models import Department,Doctors

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)