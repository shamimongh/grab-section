from django.contrib import admin
from .models import Student, Course, StudentCourse, SectionSelection

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(SectionSelection)
