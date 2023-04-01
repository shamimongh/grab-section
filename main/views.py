from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, SectionSelection

# Create your views here.
def studentHome (response):
  student = Student.objects.get(id=1)
  courses = student.studentcourse_set.all()

  context = {
    "student": student,
    "courses": courses
  }
  return render(response, "main/student/home.html", context)

def section_request(request):
  if request.method == 'POST':
    student = request.POST.get('student_id')
    course = request.POST.get('course_id')

    print(student, course)

    SectionSelection(
      student_id = student,
      course_id = course,
      section = "A",
      message = ""
    ).save()

    return HttpResponse(request.POST)
  else:
    return HttpResponse("Ah!")
    
def section_request(request):
  if request.method == 'POST':
    student = request.POST.get('student_id')
    course = request.POST.get('course_id')

    print(student, course)

    SectionSelection(
      student_id = student,
      course_id = course,
      section = "A",
      message = ""
    ).save()

    return HttpResponse(request.POST)
  else:
    return HttpResponse("Ah!")