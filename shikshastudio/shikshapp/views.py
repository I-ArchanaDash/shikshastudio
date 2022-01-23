from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from shikshapp import models
# Create your views here.

def home(request):
    response = render(request,'shikshapp/index.html')
    return response
def teacherDashboard(request):
    response =render(request,'shikshapp/teacher_dashboard.html')
    return response
def newTeacher(request):
    error_msg="Username Already Exists"
    d=()
    if request.GET['err']:
        d['error_msg']=error_msg
    response=render(request,'shikshapp/new_teacher.html',d)
    return response
def newTeacherRegistration(request):
    user=models.shikshapp_teachers()
    user.username=request.POST['username']
    if user==models.shikshapp_teachers.objects.get(username==user.username):
        s="http://localhost:8000/shikshapp/newTeacher?err=1"
        return HttpResponseRedirect(s)
    user.password=request.POST['password']
    user.save()
    return HttpResponseRedirect("http://localhost:8000/shikshapp/teacher-login")
def teacherLoginValidate(request):
    username=request.POST['username']
    password=request.POST['password']
    user=models.shikshapp_teachers.objects.get(username=username,password=password)
    if user:
        s="http://localhost:8000/shikshapp/teacher-dashboard/"
        return HttpResponseRedirect(s)
    else:
        s="http://localhost:8000/shikshapp/teacher-login/"
        return HttpResponseRedirect(s)
def teacherLogin(request):
    response=render(request,'shikshapp/teacher_login.html')
    return response
def teacherLogout(request):
    pass