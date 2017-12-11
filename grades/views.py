# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import Context,loader
from django.forms import formset_factory
from .forms import SCForm,StudentForm,CourseForm,InquireForm
from django.http import HttpResponse,JsonResponse
from .models import Student,Course,SC
from django.utils import timezone
from django.shortcuts import render_to_response
import json
from django.core.serializers import serialize

def index(request):
    now=timezone.now()
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

def inquire(request):
    if request.method=='GET':
        inquire_student=Student.objects.all().filter(student_id=request.GET['student_id'])
        response=JsonResponse({'response':serialize('json',inquire_student)})
        return response
    else:
        return JsonResponse({'e':'not found'})



def details(request):
    pass

def manager(request):
    pass
