from typing import Any

from django.shortcuts import render,redirect
from django.urls import reverse

from hospital_app.models import CustomUser,Appointment, History, TimeSlot
from hospital_app.forms import UserLoginForm,AppointmentForm, CustomUserCreationForm,TimeSlotForm,AppointmentStatusForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView,FormView ,ListView,CreateView,DetailView,DeleteView,UpdateView
from django.views.generic.edit import CreateView

from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = 'home.html'
class AppointmentViewListForPatients(TemplateView):
    template_name = 'appointment_list_view_users.html'

#view to signup for user
class UserSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user_register.html'
    success_url = reverse_lazy('hospital_app:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'User'  # Set the user_type to 'User'
        user.save()
        return super().form_valid(form)
#signup for superadmin
class SuperAdminSignupView(CreateView):
    form_class =CustomUserCreationForm
    template_name = 'superadmin_register.html'
    success_url = reverse_lazy('hospital_app:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'Super Admin'  # Set the user_type to 'Super admin'
        user.save()
        return super().form_valid(form)


#view to fill appointment form by user
class AppointmentFormView( LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = AppointmentForm
    template_name = 'booking.html'
    success_url = reverse_lazy('hospital_app:list3')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['User']
    def form_valid(self, form):
        return super().form_valid(form)

# to see list of appointments for superadmin(has create,update,delete  option)
class AppointmentListView1(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'view1.html'
    context_object_name = 'appointments'
    login_url = '/login/'


from django.views.generic import DetailView
from .models import History

class AppointmentHistoryView(DetailView):
    model = History  # This specifies the model to use
    template_name = 'appointment_history.html'  # Specify the template name
    context_object_name = 'history'  # Specify the context variable name

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(History, pk=pk)


# view to create admin
class AdminCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'create.html'
    success_url = reverse_lazy('hospital_app:list1')


    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)

#view to add time slot
class TimeSlotCreateView(CreateView):
    model = TimeSlot
    form_class = TimeSlotForm
    template_name = 'time_slot_create.html'
    success_url = reverse_lazy('hospital_app:list1')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class AppointmentStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, FormView):
    form_class = AppointmentStatusForm
    template_name = 'update_status.html'
    success_url = reverse_lazy('hospital_app:list1')

    def test_func(self):
        user_type = self.request.user.user_type
        return user_type in ['Admin', 'Super Admin']

    def form_valid(self, form):
        appointment_id = self.kwargs['appointment_id']
        status = form.cleaned_data['status']
        appointment = Appointment.objects.get(pk=appointment_id)
        appointment.status = status
        appointment.save()
        return redirect(self.success_url)



# to see list of appointments for admins(has update option)
class AppointmentListView2(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'view2.html'
    context_object_name = 'appointments'
    login_url = '/login/'

# to see  appointments options for patients(has booking option)
class AppointmentListView3(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'view3.html'
    context_object_name = 'appointments'
    login_url = '/login/'

#to see list of appointments , view made for patients
class AppointmentViewListForPatients(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'appointment_list_view_users.html'
    context_object_name = 'appointments'
    login_url = '/login/'


class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)

        if user:
            if user.user_type == 'User':
                login(self.request, user)
                list3_url = reverse('hospital_app:list3')
                return redirect(list3_url)  # Redirect to Patient Home
            elif user.user_type == 'Admin':
                login(self.request, user)
                list2_url = reverse('hospital_app:list2')
                return redirect(list2_url)  # Redirect to admin home
            elif user.user_type == 'Super Admin':
                login(self.request, user)
                list1_url = reverse('hospital_app:list1')
                return redirect(list1_url)  # Redirect to Super Admin home

        return HttpResponse("Invalid login details.....")






# view for logout
class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        logout_url = reverse('hospital_app:home')
        return redirect(logout_url)
