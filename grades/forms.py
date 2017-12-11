from django import forms
from .models import Student,Course,SC

class StudentForm(forms.Form):
    student_id=forms.CharField()
    name=forms.CharField()
    gender=forms.CharField(required=False)
    class_id=forms.CharField()

class CourseForm(forms.Form):
    course_name=forms.CharField()
    course_id=forms.CharField()
    credit=forms.FloatField()

class SCForm(forms.Form):
    student=forms.ModelMultipleChoiceField(queryset=Student.objects.all())
    course=forms.ModelMultipleChoiceField(queryset=Course.objects.all())
    score=forms.FloatField()

class InquireForm(forms.Form):
    student_id=forms.CharField(label="输入你的学号:",required=False)

