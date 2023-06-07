from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(max_length=20)
    id = models.CharField(primary_key=True, max_length=2)

    def __str__(self):
        return self.name;

class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(max_length=80)
    course_credits = models.CharField(max_length=15)

    def __str__(self):
        return self.course_id;

class Faculty(models.Model):
    faculty_fname = models.CharField(primary_key=True, max_length=50)
    faculty_sname = models.CharField(max_length=10)

    def __str__(self):
        return self.faculty_fname;