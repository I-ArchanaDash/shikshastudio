from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from shikshapp import models
# Create your views here.

def home(request):
    response = render(request,'shikshapp/index.html')
    return response
def deco_login(f1):
    def mod_f1(request):
        if 'username' in request.session.keys():
            return f1(request)
        else:
            return HttpResponseRedirect("http://localhost:800/shikshapp/teacher-login/")
    return mod_f1
def newTeacher(request):
    error_msg="Username Already Taken"
    d={}
    try:
        if int(request.GET['err'])==1:
            d['error_msg']=error_msg
    except:
        pass
    response=render(request,'shikshapp/new_teacher.html',d)
    return response
def newTeacherRegistration(request):
    user=models.shikshapp_teachers()
    user.username=request.POST['username']
    try:
        user==models.shikshapp_teachers.objects.get(username=user.username)
        s="http://localhost:8000/shikshapp/new-teacher?err=1"
        return HttpResponseRedirect(s)
    except:
        pass
    user.password=request.POST['password']
    user.save()
    return HttpResponseRedirect("http://localhost:8000/shikshapp/teacher-login")
def teacherLoginValidate(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        user=models.shikshapp_teachers.objects.get(username=username,password=password)
        s="http://localhost:8000/shikshapp/teacher-dashboard/"
        request.session['username']=username
    except:
        s="http://localhost:8000/shikshapp/teacher-login/"
    return HttpResponseRedirect(s)
def teacherLogin(request):
    response=render(request,'shikshapp/teacher_login.html')
    return response

def teacherLogout(request):
    del request.session['username']
    return HttpResponseRedirect("http://localhost:8000/")
@deco_login #checks logged in user
def teacherDashboard(request):
    response =render(request,'shikshapp/teacher_dashboard.html')
    return response