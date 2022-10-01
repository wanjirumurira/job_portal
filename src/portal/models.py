from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model): 
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(null=True,max_length=200)
    position= models.CharField(null=True,max_length=200)
    job_description= models.TextField(blank=False)
    location=models.CharField(null=True,max_length=200)
    experience=models.CharField(null=True,max_length=200)

    def __str__(self):
        return self.name



class Candidate(models.Model):
    category = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
    name= models.CharField(null=True,max_length=200)
    date_of_birth = models.DateField(null= True)
    gender= models.CharField(null=True,max_length=200,choices=category)
    phone_number= models.CharField(null= True,max_length=50)
    email=models.CharField(null=True,max_length=200, unique=True)
    resume=models.FileField(null=True,max_length=200)
    
    company= models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name