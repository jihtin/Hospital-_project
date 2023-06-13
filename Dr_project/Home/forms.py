from django import forms
from .models import Booking


class DateInput(forms.DateInput):
       input_type = 'date'

class BookingForms(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets = {
           "booking_date" : DateInput()
        }
        
        labels = {
            "p_name" : 'Patient Name',
            "p_phone" : 'patient Phone',
            "doc_name" :  'Doctor Name',
             "p_email" : 'Enter your Email',
            "booking_date":  'Booking Date'
      
        }