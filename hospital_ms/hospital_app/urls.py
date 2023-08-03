from django.urls import path

from hospital_app import views


app_name = 'hospital_app'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('booking/',views.AppointmentFormView.as_view(),name='booking'),


    path('appointmentlist1', views.AppointmentListView1.as_view(), name='list1'),
    path('appointmentlist2', views.AppointmentListView2.as_view(), name='list2'),
    path('appointmentlist3', views.AppointmentListView3.as_view(), name='list3'),
    path('appointmentlistpatients', views.AppointmentViewListForPatients.as_view(), name='list4'),

    path('update_status/<int:pk>/', views.AppointmentStatusUpdateView.as_view(), name='update_status'),


    path('appointmenthistory/<int:pk>/', views.AppointmentHistoryView.as_view(), name='ahistory'),
    path('timeslot/', views.TimeSlotCreateView.as_view(), name='add_timeslot'),
    path('createadmin', views.AdminCreateView.as_view(), name='create'),




    path('user-signup/', views.UserSignupView.as_view(), name='usersignup'),
    path('superuser-signup/', views.SuperAdminSignupView.as_view(), name='superadminsign'),

    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    ]