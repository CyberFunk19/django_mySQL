from django.db import models

class Student(models.Model):
    sName = models.CharField(max_length=50,null=True,blank=True)
    age = models.IntegerField()
    email = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['name','age','email']
 
    def __str__(self):
           return self.sName,self.age,self.email
