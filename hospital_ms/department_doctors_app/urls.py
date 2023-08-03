from django.urls import path

from department_doctors_app import views


app_name = 'department_doctors_app'

urlpatterns = [
    path('departmentlist/', views.DepartmentListView.as_view(), name='departmentlist'),
    path('create/', views.DepartmentCreateView.as_view(), name='createdepartment'),
    path('update/<int:pk>/', views.DepartmentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DepartmentDeleteView.as_view(), name='delete'),

     path('createdoctor/', views.DoctorCreateView.as_view(), name='createdoctor'),
     path('doctorlist/', views.DoctorsListView.as_view(), name='doctor_list'),
     path('doctordetail/<int:pk>/',views.DoctorDetailView.as_view(), name='doctor_detail'),


]


