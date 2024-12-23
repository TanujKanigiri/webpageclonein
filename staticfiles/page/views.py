from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def request(request):
    return render(request,'request.html')

def signin(request):
    return render(request,'signin.html')

def checkcourses(request):
    return render(request,'checkcourses.html')