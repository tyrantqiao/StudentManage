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
    #now=timezone.now()
    form=InquireForm()
    return render_to_response('grades/index.html',{'form':form})

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
        inquire_id=request.GET.get('student_id')
        print(inquire_id)
        inquire_student=Student.objects.all().filter(student_id=inquire_id)
        if inquire_student==None:
            return HttpResponse(json.dumps({'error':'not found'}),status=404)
        return  HttpResponse(inquire_student[0])
    else:
        return HttpResponse(json.dumps({'error':'notfound'}),content_type="application/json")



def details(request):
    pass

def manager(request):
    pass
