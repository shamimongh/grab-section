from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    student_id = models.CharField(primary_key=True, unique=True, max_length=255)
    student_name = models.CharField(max_length=255)
    student_password = models.CharField(max_length=255)

    def __str__(self):
        return self.student_name

class Course(models.Model):
    course_id = models.CharField(primary_key=True, unique=True, max_length=255)
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return self.course_name

class CompletedCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_id) + " | " + str(self.course_id)

class IncompleteCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.student_id) + " | " + str(self.course_id)

class Section(models.Model):
    section_id = models.CharField(primary_key=True, unique=True, max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=255)
    section_instructor = models.CharField(max_length=255)
    section_capacity = models.IntegerField()
    section_enrolled = models.IntegerField()

    def __str__(self):
        return self.section_name