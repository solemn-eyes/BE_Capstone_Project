# Here I'll be describing the views for the tracker app
from rest_framework import viewsets
from .models import Students, Courses, Enrollments, Grades
from .serializers import StudentsSerializer, CoursesSerializer, EnrollmentsSerializer, GradesSerializer

# ViewSet for Students
class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

# ViewSet for Courses
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

# ViewSet for Enrollments
class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollments.objects.all()
    serializer_class = EnrollmentsSerializer

# ViewSet for Grades
class GradesViewSet(viewsets.ModelViewSet):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

