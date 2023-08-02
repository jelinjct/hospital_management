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
    context_object_name = 'vehicles'
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
        return self.request.user.user_type in ['Super admin']
    def form_valid(self, form):
        # Set the current user as the owner of the vehicle being created
        form.instance.department = self.request.user
        return super().form_valid(form)


# view to update department
class DepartmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Department
    template_name = 'update_department.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('department_doctors_app:departmentlist')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['Super admin', 'Admin']

    def get_success_url(self):
        return reverse_lazy('department_doctors_app:detail', kwargs={'pk': self.object.pk})

# view to delete department
class DepartmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Department
    template_name = 'delete_department.html'
    success_url = reverse_lazy('user_access:departmentlist')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'
    def test_func(self):
        return self.request.user.user_type in ['Super admin']

    def get_success_url(self):
        return reverse_lazy('department_doctors_app:delete')


#view to doctors list
class DoctorsListView(View):
    def get(self, request):
        doc = Doctors.objects.all()
        return render(request, 'doctors.html', {'doc': doc})


#view to doctors detail
class DoctorDetailView(View):
    def get(self, request, pslug):
        de = get_object_or_404(Doctors, slug=pslug)
        return render(request, 'doctors_detail.html', {'de': de})
