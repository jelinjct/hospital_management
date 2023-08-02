
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hospital_app.urls')),
    path('departmentlist/',include('department_doctors_app.urls')),
]
