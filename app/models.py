from django.db import models

# Create your models here.


    
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=20)
    def __str__(self):
        return self.teacher_name
    
    
       
class Student_Registration(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    roll_no=models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name       