# Here I'll be defining the url paths for the tracker app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, GradesViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'students', StudentsViewSet)
router.register(r'courses', CoursesViewSet)
router.register(r'enrollments', EnrollmentsViewSet)
router.register(r'grades', GradesViewSet)

# The urlpatterns for the tracker app
urlpatterns = [
    path('', include(router.urls)),
]

