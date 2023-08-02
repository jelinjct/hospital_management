from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from hospital_app.models import CustomUser,Appointment, TimeSlot

admin.site.register(CustomUser)

admin.site.register(TimeSlot)


admin.site.register(Appointment)

