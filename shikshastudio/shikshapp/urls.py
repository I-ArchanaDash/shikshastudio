from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('teacher-dashboard/',views.teacherDashboard),
    path('new-teacher/',views.newTeacher),
    path('new-teacher-signup/',views.newTeacherRegistration),
    path('teacher-login-validate/',views.teacherLoginValidate),
    path('teacher-login/',views.teacherLogin),
    path('teacher-logout/',views.teacherLogout),
    path('add-work/',views.addWork),
]