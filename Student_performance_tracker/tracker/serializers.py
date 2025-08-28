# I'll be making the serializers for the models in the tracker app.
from rest_framework import serializers
from .models import Student, Course, Enrollment, Grade
from django.contrib.auth.models import User

# Serializer for Students model
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # Include all fields in the serialization

# Serializer for Courses model
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # Include all fields in the serialization

# Serializer for Enrollments model
class EnrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'  # Include all fields in the serialization

# Serializer for Grades model
class GradesSerializer(serializers.ModelSerializer):
    letter_grade = serializers.ReadOnlyField()
    class Meta:
        model = Grade
        fields = '__all__'  # Include all fields in the serialization

# Serializer for Login/Sign up registration
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

