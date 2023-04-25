from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.
link_length = 500
class Course(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Semester(models.Model):
    
    def sem_choices():
        return [(f'semester{r}',f'semester{r}') for r in range(1,9)]
    sem = models.CharField(choices=sem_choices(),max_length=50,null=True)
    def __str__(self):
        return str(self.sem)
    number = models.IntegerField(default=1,choices= ((i,i) for i in range(1,9)))
    
class Subject(models.Model):
    branch = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    semester =  models.ForeignKey(Semester,on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name

class BookLink(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=200,null=True)
    href = models.CharField(max_length= link_length)
    def __str__(self):
        return self.name

class Pyq(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True) 
    def __str__(self):
        return str(self.subject)
    

class PyqLink(models.Model):
    pyq = models.ForeignKey(Pyq,on_delete=models.CASCADE,null=True)
    def year_choices():
        return [(r,r) for r in range(1984, datetime.date.today().year+1)]

    def current_year():
        return datetime.date.today().year
    year = models.IntegerField(choices=year_choices(),default=current_year())    
    month = models.CharField(max_length=20,choices=[(i,i) for i in ['march','december']],null=True)
    href = models.CharField(max_length=500,null=True)
    
    def __str__(self):
        return str(self.year)
    
class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)
    
class Video(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails',null=True)
    description = models.TextField(max_length=500)
    url = models.CharField(max_length=500, null=False)
    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=500,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.title)