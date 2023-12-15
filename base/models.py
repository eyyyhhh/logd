from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class User(models.Model):
    usernum = models.BigIntegerField()
    username = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    birthdate = models.CharField(max_length=100)
    age = models.IntegerField()
    status = models.IntegerField(default=1)
    school_id = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    schoolName = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    mission =models.CharField(max_length=800,default="vv")
    vission =models.CharField(max_length=800,default="vv")

    def __str__(self):
        return self.name
    
class Logs(models.Model):
    userid = models.IntegerField()
    schoolid = models.IntegerField()
    temperature = models.CharField(max_length=100, default="36.8")
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    remarks = models.IntegerField()
    q1 = models.CharField(max_length=10, default="1")
    q2 = models.CharField(max_length=10, default="1")
    q3 = models.CharField(max_length=10, default="1")
    q4 = models.CharField(max_length=10, default="1")
    q5 = models.CharField(max_length=10, default="1")
    q6 = models.CharField(max_length=10, default="1")
    q7 = models.CharField(max_length=10, default="1")
    q8 = models.CharField(max_length=10, default="1")
    q9 = models.CharField(max_length=10, default="1")

    def __str__(self):
        return self.name



class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)