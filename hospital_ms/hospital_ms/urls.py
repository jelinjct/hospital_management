
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('hospital_app.urls')),
    path('departmentlist/',include('department_doctors_app.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root = settings.MEDIA_ROOT)