from django.contrib import admin
from .models import Student,SC,Course
import json
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,  {'fields':['name']}),
        ('个人信息', {'fields':['student_id','gender','class_id']})
    ]
    list_display=('name','student_id')
    list_filter=['class_id','gender']
    search_fields=['student_id','name','gender','class_id']

class CourseAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['course_name']}),
        ('课程信息',{'fields':['course_id','credit']})
    ]
    list_display=('course_name','course_id','credit')
    list_filter=['credit']
    search_fields=['course_name','course_id','credit']


class SCAdmin(admin.ModelAdmin):
    list_display=('get_students','get_courses','score')
    list_filter=('student','course')
    search_fields=('student__class_id','course__course_id','student__name','student__student_id','student__gender','course__course_name','course__credit','score')
    raw_id_fields=('student','course',)



admin.site.register(Student,StudentAdmin)
admin.site.register(SC,SCAdmin)
admin.site.register(Course,CourseAdmin)


