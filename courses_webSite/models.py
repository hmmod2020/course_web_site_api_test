from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your models here.

from django.utils import timezone


class categorie(models.Model):
    title=models.CharField(max_length=25,null=False,blank=False)

class courses(models.Model):
    title=models.TextField(max_length=25,blank=False,null=False)
    date=models.DateField(blank=True,null=True)
    by_user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=500,blank=True,null=True)
    descriptionOfRequerment=models.TextField(max_length=500,blank=True,null=True)
    afterThisCourse=models.TextField(max_length=500,blank=True,null=True)
    categorie=models.ForeignKey(categorie,on_delete=models.CASCADE)
    thumbnail=models.ImageField(null=True,blank=True)
    price=models.IntegerField(default=0,null=False,blank=False)
    avalable=models.BooleanField(default=False)
    numberOfView=models.IntegerField(default=0,blank=False,null=False)
    numberOfBuying=models.IntegerField(default=0,blank=False,null=False)



class userInfo(models.Model):
    by_user=models.OneToOneField(User,on_delete=models.CASCADE)
    fName=models.CharField(max_length=25,blank=False,null=False)
    lName=models.CharField(max_length=25,blank=False,null=False)
    education=models.TextField(max_length=100,blank=False,null=False)
    email=models.EmailField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True)
    description=models.TextField(max_length=250,blank=True,null=True)


class lessons(models.Model):
    title =models.CharField(max_length=25,blank=False,null=False)
    description=models.TextField(max_length=250,blank=True,null=True)
    video=models.FileField(upload_to='videos/%y',null=True,blank=True)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)

class files(models.Model):
    lessons=models.ForeignKey(lessons,on_delete=models.CASCADE)
    file=models.FileField(upload_to='files/%y',blank=True,null=True)

class userBoughtCourse(models.Model):
    by_user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    price=models.IntegerField(blank=False,null=False)

class commentOnCourse(models.Model):
    by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(courses, on_delete=models.CASCADE)
    comment=models.TextField(max_length=250,blank=False,null=False)

class courseUserWatch(models.Model):
    by_user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    completionRate=models.IntegerField(default=0,blank=False,null=False)

class Wallet(models.Model):
    by_user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount=models.IntegerField(blank=True,null=True)

class transaction(models.Model):
    by_wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE)
    transactionType=models.CharField(max_length=30,blank=True,null=True)
    amount=models.IntegerField(blank=True,null=True)
    create_at=models.DateField(blank=True,null=True)


class rateCourse(models.Model):
    by_user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(courses,on_delete=models.CASCADE)
    rate=models.IntegerField(blank=False,null=False,default=1)
    comment=models.ForeignKey(commentOnCourse, on_delete=models.CASCADE)

class earnings(models.Model):
    userMadeCourse=models.ForeignKey(User,on_delete=models.CASCADE)
    totalFullBalunse=models.IntegerField(default=0)
    avalableFullBalunse=models.IntegerField(default=0)
    avalableBalunse=models.IntegerField(default=0)
