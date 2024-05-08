from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_class/', views.create_class, name='create_class'),
    path('add_student/<int:class_id>/', views.add_student_to_class, name='add_student'),
    path('record_attendance/<int:class_id>/', views.record_attendance, name='record_attendance'),
    path('create_assignment/<int:class_id>/', views.create_assignment, name='create_assignment'),
    path('grade_student/<int:assignment_id>/', views.grade_student, name='grade_student'),
]
