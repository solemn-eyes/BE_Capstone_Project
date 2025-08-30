# Here I'll be describing the views for the tracker app
from rest_framework import viewsets
from .models import Student, Course, Enrollment, Grade
from .serializers import StudentsSerializer, CoursesSerializer, EnrollmentsSerializer, GradesSerializer
from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

# ViewSet for Students
class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

# ViewSet for Courses
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer

# ViewSet for Enrollments
class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentsSerializer

# ViewSet for Grades
class GradesViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradesSerializer

@api_view
def student_mean_score(request, student_id):
    mean_score = Grade.objects.filter(Enrollments__Students__id=student_id).aggregate(Avg('score'))
    return Response({
        "student_id":student_id,
        "mean_score":mean_score['score_avg']
    })

@api_view
def course_mean_score(request, course_id):
    mean_score = Course.objects.filter(Enrollments__Courses__id=course_id).aaggregate(Avg('score'))
    return Response({
        "course_id":course_id,
        "mean_score":mean_score['score_avg']
    })

# Setting the courses to be viewed by anyone
class PublicCourseList(APIView):
    permission_classes = [AllowAny]

# Creating a view for user(to create new user when getting authentication)
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user
    
# A view for the registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]