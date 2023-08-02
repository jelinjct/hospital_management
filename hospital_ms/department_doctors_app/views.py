from django.shortcuts import render
from department_doctors_app.models import Department,Doctors
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView ,TemplateView,View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View



class DepartmentListView( ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departmentList'
    login_url = '/login/'

#view to create department
class DepartmentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Department
    template_name = 'create_department.html'
    fields = ['department_name', 'department_description']
    success_url = reverse_lazy('department_doctors_app:departmentlist')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['Super Admin']
    def form_valid(self, form):
        form.instance.department = self.request.user
        return super().form_valid(form)


# view to update department, both Admin and Super Admin can update
class DepartmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Department
    template_name = 'update_department.html'
    fields = ['department_name','department_description']
    success_url = reverse_lazy('department_doctors_app:departmentlist')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['Super Admin', 'Admin']

    def get_success_url(self):
        return reverse_lazy('department_doctors_app:departmentlist')

# view to delete department
class DepartmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Department
    template_name = 'delete_department.html'
    success_url = reverse_lazy('department_doctors_app:departmentlist')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'
    def test_func(self):
        return self.request.user.user_type in ['Super Admin', 'Admin']

    def get_success_url(self):
        return reverse_lazy('department_doctors_app:departmentlist')

#view to create doctor
class DoctorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Doctors
    template_name = 'create_doctor.html'
    fields = ['doctor_name', 'doctor_department_fk','qualification','photo']
    success_url = reverse_lazy('department_doctors_app:doctor_list')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['Super Admin']
    def form_valid(self, form):
        return super().form_valid(form)

#view to doctors list
class DoctorsListView( ListView):
    model = Doctors
    template_name = 'doctors.html'
    context_object_name = 'doctorList'
    login_url = '/login/'

#view to doctors detail
class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctors
    template_name = 'doctors_detail.html'
    context_object_name = 'doctorr'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('department_doctors_app:doctor_detail')