from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Class, Student, Attendance, Assignment, Grade
from .forms import ClassForm, StudentForm, AttendanceForm, AssignmentForm, GradeForm

@login_required
def dashboard(request):
    if request.user.is_superuser:
        # Admin view
        classes = Class.objects.all()
        students = Student.objects.all()
        assignments = Assignment.objects.all()
        return render(request, 'admin_dashboard.html', {'classes': classes, 'students': students, 'assignments': assignments})
    else:
        # Teacher view
        classes = Class.objects.filter(teacher=request.user)
        return render(request, 'teacher_dashboard.html', {'classes': classes})

@login_required
def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.teacher = request.user
            new_class.save()
            messages.success(request, 'Class created successfully!')
            return redirect('dashboard')
    else:
        form = ClassForm()
    return render(request, 'create_class.html', {'form': form})

@login_required
def add_student_to_class(request, class_id):
    school_class = Class.objects.get(pk=class_id)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            school_class.students.add(student)
            messages.success(request, f'Student {student.user.username} added to {school_class.name}')
            return redirect('dashboard')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form, 'school_class': school_class})

@login_required
def record_attendance(request, class_id):
    school_class = Class.objects.get(pk=class_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance recorded successfully!')
            return redirect('dashboard')
    else:
        form = AttendanceForm()
    return render(request, 'record_attendance.html', {'form': form, 'school_class': school_class})

@login_required
def create_assignment(request, class_id):
    school_class = Class.objects.get(pk=class_id)
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.class_assigned = school_class
            assignment.save()
            messages.success(request, 'Assignment created successfully!')
            return redirect('dashboard')
    else:
        form = AssignmentForm()
    return render(request, 'create_assignment.html', {'form': form, 'school_class': school_class})

@login_required
def grade_student(request, assignment_id):
    assignment = Assignment.objects.get(pk=assignment_id)
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Grade recorded successfully!')
            return redirect('dashboard')
    else:
        form = GradeForm(initial={'assignment': assignment})
    return render(request, 'grade_student.html', {'form': form, 'assignment': assignment})
