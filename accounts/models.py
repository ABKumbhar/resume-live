from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model ):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    



class Projects(models.Model):
    name = models.CharField(max_length = 200,null=True)
    description = models.TextField()
    startdate = models.CharField(max_length=20,null=True)
    enddate = models.CharField(max_length=20,null=True)
    Files = models.FileField(upload_to='images/',null=True, verbose_name="",blank=True)
    customer = models.ForeignKey(Customer,null=True, on_delete = models.SET_NULL)
    def __str__(self):
        return self.name

class Achievement(models.Model):
    name = models.TextField()
    customer = models.ForeignKey(Customer,null=True, on_delete = models.SET_NULL)
    def __str__(self):
        return self.name

class Grades(models.Model):
    customer = models.ForeignKey(Customer,null=True, on_delete = models.SET_NULL)
    total = models.FloatField(default=9.717)
    branch = models.CharField(max_length=200,default="Chemical Engineering")
    Institute = models.CharField(max_length=200,default = 'Indian Institute of Technology, Roorkee')
    lastsemester = models.FloatField(default=9.69)



class ExtraCurricular(models.Model):
    name = models.CharField(max_length = 200,null=True)
    description = models.TextField()
    startdate = models.CharField(max_length=20,null=True)
    enddate = models.CharField(max_length=20,null=True)
    Files = models.FileField(upload_to='images/',null=True, verbose_name="",blank=True)
    customer = models.ForeignKey(Customer,null=True, on_delete = models.SET_NULL)

    def __str__(self):
            return self.name
