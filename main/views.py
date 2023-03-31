from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, CompletedCourse, IncompleteCourse

# Create your views here.
def studentHome (response):
  student = Student.objects.get(student_id= '1')
  comCourses = CompletedCourse.objects.filter(student_id=student)
  incomCourses = IncompleteCourse.objects.filter(student_id=student)

  context = {
    'student': student,
    'comCourses': comCourses,
    'incomCourses': incomCourses
  }
  
  return render(response, "main/student/home.html", context)