from django.shortcuts import render

# Create your views here.

def home(request):
    response = render(request,'shikshapp/index.html')
    return response