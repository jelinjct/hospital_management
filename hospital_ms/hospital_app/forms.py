from django.contrib.auth.forms import UserCreationForm

from hospital_app.models import CustomUser, Appointment, TimeSlot
from department_doctors_app.models import Department, Doctors
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)




#appointment booking form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = (
            'TokenNo',
            'patient_name',
            'patient_email',
            'patient_phone',
            'patient_place',
            'appointment_date',
            'appointment_time',
            'patient_department',
            'doctor',

        )

    patient_department = forms.ChoiceField(
        label='Choose Department',
        choices=[('ortho', 'orthopedics'), ('cardio', 'Cardiology'),
                   ('derma', 'Dermatology'), ('Gynec', 'Gynecology'), ])

    doctor = forms.ModelChoiceField(
        label='Choose A Doctor',
        queryset=Doctors.objects.all(),
        empty_label='Select a doctor'
    )

    # Adding a widget for the appointment_date field
    appointment_date = forms.DateField(
        label='Appointment Date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = [ 'start_time', 'end_time']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and start_time >= end_time:
            raise forms.ValidationError("End time must be after start time.")

        return cleaned_data


class AppointmentStatusForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
