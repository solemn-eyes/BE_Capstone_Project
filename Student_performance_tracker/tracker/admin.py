# Here I'll just be registering the models for the admin interface.
from django.contrib import admin
from .models import Student, Course, Enrollment, Grade

# Registering the models to make them accessible in the admin interface
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Grade)

