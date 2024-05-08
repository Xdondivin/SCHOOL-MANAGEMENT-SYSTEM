from django import forms
from .models import Class, Student, Attendance, Assignment, Grade

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'present', 'class_attendance']

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['assignment', 'student', 'score']
