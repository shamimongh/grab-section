from django.contrib import admin
from .models import Student, Course, StudentCourse, SectionSelection, Mentor

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(StudentCourse)
admin.site.register(SectionSelection)
