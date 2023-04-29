from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student, SectionSelection, Mentor

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
    section = request.POST.get('section')

    print(student, course)

    isExist = SectionSelection.objects.filter(student_id=student, course_id=course).exists()

    if isExist:
      data = SectionSelection.objects.filter(student_id=student, course_id=course)
      data.delete()
    else:
      SectionSelection(
        student_id = student,
        course_id = course,
        section = section,
        message = ""
      ).save()

      return HttpResponse(request.POST)
  else:
    return HttpResponse("Ah!")

def requested_section(request):
  if request.method == 'POST':
    student_id = request.POST.get('student_id')

    data = SectionSelection.objects.filter(student_id=student_id).values()
    print(data)

    return JsonResponse(list(data), safe=False)

  else:
    return HttpResponse("Ah!")
  
def mentorHome(request):
  mentor = Mentor.objects.get(id=1)
  # student_data = SectionSelection.objects.order_by().values('student').distinct()
  student_data = SectionSelection.objects.all().values('student').distinct()

  print(student_data)

  context = {
    "mentor": mentor,
    "student_data": student_data,
  }
  return render(request, 'main/mentor/home.html', context)


