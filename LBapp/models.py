from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=100)
    booknumber=models.IntegerField(default=None, blank=True, null=True)
    author=models.CharField(max_length=50,default=None, blank=True, null=True)
    date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    price=models.FloatField()
    quantity=models.IntegerField(default=None, blank=True, null=True)
    def __str__(self):
        return self.name
class libraryuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,null=False)
class issuebook(models.Model):
    studentid=models.CharField(max_length=10)
    sname=models.CharField(max_length=20,null=False)
    bookname=models.CharField(max_length=100)
    booknumber=models.IntegerField(default=None, blank=True, null=True)
    author=models.CharField(max_length=50)
    issuedate=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    returndate=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    aquantity=models.IntegerField()
    def __str__(self):
        return self.bookname
class returnbook(models.Model):
    studentid=models.CharField(max_length=10)
    sname=models.CharField(max_length=20,default=None, blank=True, null=True)
    bookname=models.CharField(max_length=20,null=False)
    booknumber=models.IntegerField(default=None, blank=True, null=True)
    author=models.CharField(max_length=50,default=None, blank=True, null=True)
    issuedate=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    returningdate=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    returneddate=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    latefee=models.FloatField(blank=True)
    def __str__(self):
        return self.bookname
