from django.shortcuts import render,redirect
from django.urls import reverse
from hospital_app.models import CustomUser,Appointment, History, TimeSlot
from hospital_app.forms import UserLoginForm,AppointmentForm, CustomUserCreationForm,TimeSlotForm
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
class AppointmentFormView(FormView):
    form_class = AppointmentForm
    template_name = 'booking.html'

    def form_valid(self, form):
            user = form.save(commit=False)
            user.user_type = 'Users'  # Set the user_type to 'User'
            user.save()
            return super().form_valid(form)



# to see list of appointments for superadmin(has create,update,delete  option)
class AppointmentListView1(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'view1.html'
    context_object_name = 'appointments'
    login_url = '/login/'


# view to history (only for superadmin)
class AppointmentHistoryView(DetailView):
    model = History
    template_name = 'appointment_history.html'
    context_object_name='history'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('hospital_app:ahistory', kwargs={'pk': self.object.pk})

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

        return super().form_valid(form)



# to see list of appointments for admins(has update option)
class AppointmentListView2(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'view2.html'
    context_object_name = 'appointments'
    login_url = '/login/'

# to see list of appointments for patients(has booking option)
class AppointmentListView3(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'view3.html'
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
                return redirect(list3_url)  # Redirect to Vehiclelist1View
            elif user.user_type == 'Admin':
                login(self.request, user)
                list2_url = reverse('hospital_app:list2')
                return redirect(list2_url)  # Redirect to VehicleList3View
            elif user.user_type == 'Super Admin':
                login(self.request, user)
                list1_url = reverse('hospital_app:list1')
                return redirect(list1_url)  # Redirect to VehicleCreateView

        return HttpResponse("Invalid login details.....")






# view for logout
class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        logout_url = reverse('hospital_app:home')
        return redirect(logout_url)
