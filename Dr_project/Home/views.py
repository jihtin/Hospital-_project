from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctors
from .forms import BookingForms

# Create your views here.
def index(request):
    return  render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    form = BookingForms()
    dict_form={
        'form' : form
    }
    return render(request,'booking.html',dict_form)
     
 
def contact(request):
    return render(request,'contact.html')

def doctors(request):
     dict_doc ={
         'doc':Doctors.objects.all()  # forlooin in doctors html page doc all thing come to doc  
     }
     return render(request,'doctors.html',dict_doc)

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)
