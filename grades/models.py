from django.db import models
from .manager import SQLManager
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    student_id=models.CharField(max_length=20)
    class_id=models.CharField(max_length=20)
    gender=models.CharField(max_length=6)
    #message
    def __str__(self):
        return self.name+','+self.student_id+','+self.gender+','+self.class_id

class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_id=models.CharField(max_length=20)
    credit=models.FloatField(default=0)
    #message
    def __str__(self):
        return self.course_name+','+self.course_id+"'s credit is"+str(self.credit)

class SC(models.Model):
    #如果我们连接到student单个属性会不会更好呢?有待测试
    student=models.ManyToManyField(Student)
    course=models.ManyToManyField(Course)
    score=models.FloatField(default=0)

    SQLS=SQLManager()
    '''
        str
    '''
    def __str__(self):
        return "student:%s 's course (%s) 's score is%f"%(self.student.__str__,self.course.__str__,self.score)



