from django.db import models

# Create your models here.

class AddHostel(models.Model):
    Hostel_id = models.AutoField(primary_key=True)
    Hostel_name = models.CharField(max_length=25)

class AddMess(models.Model):
    Mess_id = models.AutoField(primary_key=True)
    Mess_name = models.CharField(max_length=25)

class RegisterHostel(models.Model):
    studentId = models.CharField(max_length=20)
    studentName = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    contact = models.CharField(max_length=20)
    HostelName = models.CharField(max_length=20)
    MessName = models.CharField(max_length=20)

class StudentFeedback(models.Model):
    studentid = models.CharField(max_length=20)
    feedback = models.CharField(max_length=200)

