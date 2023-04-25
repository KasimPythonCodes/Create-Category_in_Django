from django.shortcuts import render ,redirect
from app.models import Student_Registration , Teacher
# Create your views here.

def Student_Views(request):
    obj=Student_Registration.objects.all()
    obj_t=Teacher.objects.all()
    
    return render(request , 'home.html' , {'obj':obj ,'obj_t':obj_t})

def Student_Add(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        roll_no = request.POST.get('roll_no')
        select_teacher_name = request.POST.get('select_teacher_name')
        obj_T =Teacher.objects.get(id=select_teacher_name) # error handle ### Cannot assign "'shandeep sharma'": "Student_Registration.teacher" must be a "Teacher" instance.###
        
        
        print(select_teacher_name ,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        
        obj=Student_Registration(first_name=first_name,last_name=last_name,email=email ,roll_no=roll_no ,teacher=select_teacher_name )
        obj.save()
        return redirect(Student_Views)
        
    return render(request , 'home.html')
        
        
def Teacher_Add(request):
    if request.method == 'POST':
        teacher_name =request.POST.get('teacher_name')
        obj=Teacher(teacher_name=teacher_name)
        obj.save()
        return redirect(Student_Views)
    return render(request , 'home.html')