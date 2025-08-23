from django.db import models

# Create your models here.

# Students model
class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

# Courses model
class Courses(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    credits = models.IntegerField()

# Enrollments model
class Enrollments(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

# Grades model
class Grades(models.Model):
    grade_id = models.AutoField(primary_key=True)
    enrollment_id = models.ForeignKey(Enrollments, on_delete=models.CASCADE)
    grade_value = models.CharField(max_length=2)  # e.g., A, B, C, etc.
    grade_date = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()

    # Incorporating a grading logic
    @property
    def letter_grade(self):
        if self.score >= 70:
            return "A"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C"
        elif self.score >= 40:
            return "D"
        else:
            return "F"
    def __str__(self):
        return f"{self.Enrollments.Students.name} - {self.letter_grade}"

    class Meta:
        unique_together = ('enrollment_id', 'grade_value')  # Ensures one grade per enrollment
