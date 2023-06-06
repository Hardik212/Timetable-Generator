from django.shortcuts import render
from django.http import HttpResponse
from core.models import Program
from django.contrib import messages
# from core.forms import programforms
import time

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
    showall=Program.objects.all().order_by('id')
    return render(request, 'program_master.html',{"data":showall})


################################ COURSE MASTER ################################
