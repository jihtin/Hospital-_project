from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_description = models.TextField(max_length=255)
    
    def __str__(self):
        return self.dept_name
        
     
class Doctors(models.Model):
    doc_name = models.CharField(max_length=100)
    dept_name = models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_spec =  models.CharField(max_length=100)
    doc_img = models.ImageField(upload_to='doctors')
     
    def __str__(self):
        return self.doc_name    