from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Class, Student, Attendance, Assignment, Grade

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(Assignment)
admin.site.register(Grade)
