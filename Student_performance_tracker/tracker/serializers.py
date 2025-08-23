# I'll be making the serializers for the models in the tracker app.
from rest_framework import serializers
from .models import Students, Courses, Enrollments, Grades

# Serializer for Students model
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'  # Include all fields in the serialization

# Serializer for Courses model
class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'  # Include all fields in the serialization

# Serializer for Enrollments model
class EnrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollments
        fields = '__all__'  # Include all fields in the serialization

# Serializer for Grades model
class GradesSerializer(serializers.ModelSerializer):
    letter_grade = serializers.ReadOnlyField()
    class Meta:
        model = Grades
        fields = '__all__'  # Include all fields in the serialization

