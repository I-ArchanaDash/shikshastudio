from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from shikshapp import models
from shikshapp.forms import worklistForm
from shikshapp.models import worklist
# Create your views here.

def home(request):
    response = render(request,'shikshapp/index.html')
    return response
def deco_login(f1):
    def mod_f1(request):
        if 'email' in request.session.keys():
            return f1(request)
        else:
            return HttpResponseRedirect("http://localhost:800/shikshapp/teacher-login/")
    return mod_f1
def newTeacher(request):
    error_msg="Email Already Taken"
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
    user.email=request.POST['email']
    try:
        user==models.shikshapp_teachers.objects.get(email=user.email)
        s="http://localhost:8000/shikshapp/new-teacher?err=1"
        return HttpResponseRedirect(s)
    except:
        pass
    user.password=request.POST['password']
    user.save()
    return HttpResponseRedirect("http://localhost:8000/shikshapp/teacher-login")
def teacherLoginValidate(request):
    email=request.POST['email']
    password=request.POST['password']
    try:
        user=models.shikshapp_teachers.objects.get(email=email,password=password)
        s="http://localhost:8000/shikshapp/teacher-dashboard/"
        request.session['email']=email
    except:
        s="http://localhost:8000/shikshapp/teacher-login/"
    return HttpResponseRedirect(s)
def teacherLogin(request):
    response=render(request,'shikshapp/teacher_login.html')
    return response

def teacherLogout(request):
    del request.session['email']
    return HttpResponseRedirect("http://localhost:8000/")
@deco_login #checks logged in user
def teacherDashboard(request):
    if request.user.is_authenticated:
        user = request.user
        form = worklistForm()
        worklists = worklist.objects.all()
        response =render(request,'shikshapp/teacher_dashboard.html',context={'form' : form , 'worklists':worklists} )
        return response
@deco_login
def addWork(request):
    try:
        username=request.POST['email']
        print(email)
    except:
        pass
    form = worklistForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        worklist = form.save(commit=False)
        worklist.email = email
        worklist.save()
        print(worklist)
        return HttpResponseRedirect("http://localhost:8000/shikshapp/teacher-dashboard/")
    else:
        return render(request,'shikshapp/teacher_dashboard.html',context={'form' : form})
