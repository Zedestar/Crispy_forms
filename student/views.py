from django.shortcuts import render, redirect
from .forms import AddStudent
from .models import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AddStudent(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("student:personalData")
    else:
        form = AddStudent()
    context = {
        'form':form,
    }
    return render(request, 'student/index.html', context=context)

def personalData(request):
    canditateData = Candidate.objects.all()
    context = {
        'data':canditateData,
    }
    return render(request, 'student/candidateData.html', context=context)