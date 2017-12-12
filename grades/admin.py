from django.contrib import admin
from .models import Student,SC,Course
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,  {'fields':['name']}),
        ('个人信息', {'fields':['student_id','gender']})

    ]


admin.site.register(Student,StudentAdmin)
admin.site.register(SC)
admin.site.register(Course)


