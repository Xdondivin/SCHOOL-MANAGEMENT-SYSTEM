from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes')
    
    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classes = models.ManyToManyField(Class, related_name='students')
    
    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
    class_attendance = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendance_records')
    
    def __str__(self):
        return f"{self.student.user.username} - {self.class_attendance.name} - {self.date}"

class Assignment(models.Model):
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    
    def __str__(self):
        return self.title

class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    score = models.FloatField()
    
    def __str__(self):
        return f"{self.student.user.username} - {self.assignment.title}: {self.score}"
