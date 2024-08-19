from django.shortcuts import render
from .models import Student
from .forms import StudentInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q




# Create your views here.
def list_student(request):
    student = Student.objects.all()
    
    
    return render(request, "student_manage/list_student.html", {"student": student})

def update_student(request,id):
    if request.method == "POST":
         
        student = Student.objects.get(pk=id)
        student_form = StudentInfoForm(request.POST,instance=student)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect("/")
    else:
        student = Student.objects.get(pk=id)
        student_form = StudentInfoForm(instance=student)
                
    return render(request, "student_manage/update_student.html", {"form": student_form})


def delete_student(request, id):
    if request.POST: 
        student = Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect("/")
        

def add_student(request):
    if request.POST:
        
        student_form = StudentInfoForm(request.POST)
        if student_form.is_valid():
            student_form.save()
            return HttpResponseRedirect("/")
    else:
        student_form = StudentInfoForm()
        
    return render(request, "student_manage/add_student.html", {"form": student_form})

def search_student(request):
    if request.POST:
        search = request.POST.get("output")
        student = Student.objects.all()
        std = None
        
        if search:
            std = student.filter(
                Q(fname__icontains = search)|
                Q(lname__icontains = search)|
                Q(email__icontains = search)|
                Q(phone__icontains = search)|
                Q(branch__icontains = search))
            
        return render(request, "student_manage/list_student.html", {"student": std})
    else:
        return HttpResponse("An error occured!!!")    
                     

