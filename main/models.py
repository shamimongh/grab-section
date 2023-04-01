from django.db import models

# Create your models here.

class Student(models.Model):
  student_id = models.IntegerField()
  student_name = models.CharField(max_length=50)

  def __str__(self):
    return self.student_name

class Course(models.Model):
  course_id = models.IntegerField()
  course_name = models.CharField(max_length=50)

  def __str__(self):
    return self.course_name

class StudentCourse(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)

  def __str__(self):
    return self.student.student_name + " " + self.course.course_name

class SectionSelection(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  section = models.CharField(max_length=50)
  status = models.CharField(default="pending", max_length=50)
  message = models.CharField(max_length=50)

  def __str__(self):
    return self.student.student_name + " " + self.course.course_name + " " + self.section