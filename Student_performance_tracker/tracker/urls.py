# Here I'll be defining the url paths for the tracker app
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, GradesViewSet, student_mean_score, course_mean_score, RegisterView
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'students', StudentsViewSet)
router.register(r'courses', CoursesViewSet)
router.register(r'enrollments', EnrollmentsViewSet)
router.register(r'grades', GradesViewSet)

# The urlpatterns for the tracker app
urlpatterns = [
    path('', include(router.urls)),
    path('students/<int:student_id>/mean_score/', student_mean_score, name='student_mean_score'),
    path('courses/<int:course_id>/mean_score/', course_mean_score, name='course_mean_score'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]

