from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Program, Course, Faculty
from django.contrib import messages
from csv import DictReader
from django.core.management import BaseCommand
# from core.forms import programforms
import time
import csv

# Create your views here.
def index(request):
    return render(request, 'index.html')

################################ PROGRAM MASTER ################################

def program_master(request):
    showall=Program.objects.all().order_by('id')
    return render(request, 'program_master.html',{"data":showall})

def insert_program(request):
    if request.method=="POST":
        if request.POST.get('id') and request.POST.get('name'):
            saverecord=Program()
            saverecord.id=request.POST.get('id')
            saverecord.name=request.POST.get('name')
            saverecord.save()
            messages.success(request,'Program '+saverecord.name+ ' with ID '+saverecord.id+ ' is saved successfully..!')
            return render(request,'insert_program.html')
    else :
        return render(request,'insert_program.html')

def edit_program(request,id):
    editprogramobj=Program.objects.get(id=id)
    return render(request,'edit_program.html',{"Program":editprogramobj})

def update_program(request,id):
    program = Program.objects.filter(name=id).update(id=request.POST.get('program_id'))
    time.sleep(5)
    return render(request, 'edit_program.html',{"Program":program})

################################ COURSE MASTER ################################

def course_master(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
        else:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            header = next(reader, None)
            for row in reader:
                course=Course(course_id=row[0], course_name=row[1], course_credits=row[2])  
                if(Course.objects.filter(course_id=row[0]).exists()):
                    Course.objects.filter(course_id=row[0]).update(course_name=row[1], course_credits=row[2])
                else:
                    course.save()
            messages.success(request,'File imported successfully..!')
            time.sleep(3)
    
    showall=Course.objects.all().order_by('course_id')
    return render(request, 'course_master.html',{"data":showall})

def insert_course(request):
    if request.method=="POST":
        if request.POST.get('course_id') and request.POST.get('course_name') and request.POST.get('course_credits'):
            saverecord=Course()
            saverecord.course_id=request.POST.get('course_id')
            saverecord.course_name=request.POST.get('course_name')
            saverecord.course_credits=request.POST.get('course_credits')
            saverecord.save()
            messages.success(request,'Course "'+saverecord.course_name+ '" with Course No. "'+saverecord.course_id+ '" is saved successfully..!')
            return render(request,'insert_course.html')
    else :
        return render(request,'insert_course.html')

def edit_course(request, id):
    editcourseobj=Course.objects.get(course_id=id)
    return render(request,'edit_course.html',{"Course":editcourseobj})

def update_course(request, id):
    course = Course.objects.filter(course_id=id).update(course_name=request.POST.get('course_name'), course_credits=request.POST.get('course_credits'))
    time.sleep(5)
    return render(request, 'edit_course.html',{"Course":course})

# def delete_course(request, id):
#     Course.objects.filter(course_id=id).delete()
#     showall = Course.objects.all().order_by('course_id')
    # return render(request, 'course_master.html',{"data":showall})

################################ FACULTY MASTER ################################

def faculty_master(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
        else:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            header = next(reader, None)
            for row in reader:
                faculty=Faculty(faculty_fname=row[0], faculty_sname=row[1])  
                if(Faculty.objects.filter(faculty_fname=row[0]).exists()):
                    Faculty.objects.filter(faculty_fname=row[0]).update(faculty_sname=row[1])
                else:
                    faculty.save()
            messages.success(request,'File imported successfully..!')
            time.sleep(3)
    
    showall=Faculty.objects.all().order_by('faculty_fname')
    return render(request, 'faculty_master.html',{"data":showall})

def insert_faculty(request):
    if request.method=="POST":
        if request.POST.get('faculty_fname') and request.POST.get('faculty_sname'):
            saverecord=Faculty()
            saverecord.faculty_fname=request.POST.get('faculty_fname')
            saverecord.faculty_sname=request.POST.get('faculty_sname')
            saverecord.save()
            messages.success(request,'Faculty "'+saverecord.faculty_fname+ '" with short name "'+saverecord.faculty_sname+ '" is saved successfully..!')
            return render(request,'insert_faculty.html')
    else :
        return render(request,'insert_faculty.html')

def edit_faculty(request, id):
    editfacultyobj=Faculty.objects.get(faculty_fname=id)
    return render(request,'edit_faculty.html',{"Faculty":editfacultyobj})

def update_faculty(request, id):
    faculty = Faculty.objects.filter(faculty_fname=id).update(faculty_sname=request.POST.get('faculty_sname'))
    time.sleep(5)
    return render(request, 'edit_faculty.html',{"Faculty":faculty})