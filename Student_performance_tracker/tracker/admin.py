# Here I'll just be registering the models for the admin interface.
from django.contrib import admin
from .models import Students, Courses, Enrollments, Grades

# Registering the models to make them accessible in the admin interface
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Enrollments)
admin.site.register(Grades)

