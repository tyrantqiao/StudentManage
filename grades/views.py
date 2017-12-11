# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import Context,loader
from django.forms import formset_factory
from .forms import SCForm,StudentForm,CourseForm,InquireForm
# Create your views here.
from django.http import HttpResponse
from .models import Student,Course,SC
from django.utils import timezone
from django.shortcuts import render_to_response
def index(request):
    now=timezone.now()
    if request.method=='GET':
       form=InquireForm(request.GET)
       if form.is_valid():
           #cd=form.cleanned_data
           print(form['student_id'])
           student=Student.objects.all().filter(student_id=form['student_id'])
           return render_to_response('grades/welcome.html',{'inquire_student':student,'form':form})
    else:
        form=InquireForm()
    return render_to_response('grades/welcome.html',{'nowtime':now,'form':form})

    '''
    if 'student_id' in request.GET:
        now=timezone.now()
        inquire_id=request.GET['student_id']
        inquire_student=Student.objects.filter(student_id=inquire_id)
        return render_to_response('grades/welcome.html',
                                  {'student':inquire_student,'query':student_id,'nowtime':now})
    '''

def lists(request):
    nowtime=timezone.now()
    all_students=Student.objects.all()
    return render(request,'grades/lists.html',{'all_students':all_students,'nowtime':nowtime})

def details(request):
    pass

def manager(request):
    pass
