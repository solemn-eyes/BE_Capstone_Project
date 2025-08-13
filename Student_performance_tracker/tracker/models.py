from django.db import models

# Create your models here.

# Students model
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

# Courses model
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField()

# Enrollments model
class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

# Grades model
class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    grade_value = models.CharField(max_length=2)  # e.g., A, B, C, etc.
    grade_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('enrollment_id', 'grade_value')  # Ensures one grade per enrollment
