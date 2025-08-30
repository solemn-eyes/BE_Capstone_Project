# BE_Capstone_Project
Hello there👋.
This repo has the Student Performance Tracker project. 
The project is an API that can be used to monitor students' grades and performance.
The models defined in the  project are Students, Courses, Enrollments and Grades. There's also a simple authentication using JWT.
The project also follows the Django REST Framework and CRUD endpoints.

To test the project's endpoints (GET, POST, PUT, DELETE) using Postman, one needs to get authenticated first.
To get authenticated the user will have to input there username and password. To do that on Postman:
    ---Copy the url : http://127.0.0.1:8000/api/register/ and put in the POST endpoint
    ---At the Body -> raw -> JSON use this :
        {
          "username": "<your-username>",
          "email": "<your-email>",
          "password": "<your-password>"
        }
    ---After creating the account, get authentication. Copy the url : http://127.0.0.1:8000/api/token/
    ---At JSON:
        {
        "username": "<your-username>",
        "password": "<your-password>"
        }
    ---After getting the access token, at the headers add:
        Authentication:    Bearer <your-access-token>

After getting authentication, the user can now access the various functions of the API.
The user can add, edit and delete a Student, Course, Enrollment or Grade record.
**To create a new student record**:
    ---Copy the url in the  POST endpoint : http://127.0.0.1:8000/api/students/
    ---Body (JSON )
        {
          "first_name": "firstName", 
          "last_name": "lastName",
          "email": "yourEmail",
          "date_of_birth": "YYYY-MM-DD"
        }
**To update a student**:
    ---PUT http://127.0.0.1:8000/api/students/2/
    ---Body (JSON)
        {
          "first_name": "firstName", 
          "last_name": "lastName",
          "email": "yourEmail",
          "date_of_birth": "YYYY-MM-DD"
        }
**To delete a student record**:
    ---DELETE http://127.0.0.1:8000/api/students/3/
**To create a new course record**:
    ---POST http://127.0.0.1:8000/api/courses/
    ---Body (JSON)
        {
          "course_name": "name",
          "course_code": "code",
          "description": "description",
          "credits": "credits"
        }
**To add a new Enrollment**:
    ---POST http://127.0.0.1:8000/api/enrollments/
    ---Body (JSON)
        {
          "student_id": "id",
          "course_id": "id"
        }
**To add a new Grade**:
    ---POST http://127.0.0.1:8000/api/grades/
    ---Body (JSON)
        {
          "enrollment_id": "id",
          "score": "the score"
        }

So far that's what the Student Performance Tracker API can do. 
Stay posted for **Updates!!**😁✅
