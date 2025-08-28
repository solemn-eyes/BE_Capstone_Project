
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AuthTests(APITestCase):
	def test_register(self):
		url = reverse('register')
		data = {
			'username': 'testuser',
			'email': 'testuser@example.com',
			'password': 'testpass123',
			'role': 'student'
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertTrue(User.objects.filter(username='testuser').exists())

	def test_login(self):
		# Register user first
		User.objects.create_user(username='loginuser', email='login@example.com', password='loginpass123')
		url = reverse('token_obtain_pair')
		data = {
			'username': 'loginuser',
			'password': 'loginpass123'
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn('access', response.data)
		self.assertIn('refresh', response.data)


class StudentCRUDTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='cruduser', password='crudpass')
		url = reverse('token_obtain_pair')
		resp = self.client.post(url, {'username': 'cruduser', 'password': 'crudpass'}, format='json')
		self.token = resp.data['access']
		self.auth = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

	def test_student_crud(self):
		# POST
		post_data = {
			'first_name': 'John',
			'last_name': 'Doe',
			'email': 'john.doe@example.com',
			'date_of_birth': '2000-01-01'
		}
		post_resp = self.client.post('/students/', post_data, format='json', **self.auth)
		self.assertEqual(post_resp.status_code, status.HTTP_201_CREATED)
		student_id = post_resp.data['student_id']

		# GET list
		get_resp = self.client.get('/students/', **self.auth)
		self.assertEqual(get_resp.status_code, status.HTTP_200_OK)
		self.assertTrue(any(s['student_id'] == student_id for s in get_resp.data))

		# GET detail
		detail_resp = self.client.get(f'/students/{student_id}/', **self.auth)
		self.assertEqual(detail_resp.status_code, status.HTTP_200_OK)
		self.assertEqual(detail_resp.data['first_name'], 'John')

		# PUT
		put_data = post_data.copy()
		put_data['first_name'] = 'Jane'
		put_resp = self.client.put(f'/students/{student_id}/', put_data, format='json', **self.auth)
		self.assertEqual(put_resp.status_code, status.HTTP_200_OK)
		self.assertEqual(put_resp.data['first_name'], 'Jane')

		# DELETE
		del_resp = self.client.delete(f'/students/{student_id}/', **self.auth)
		self.assertEqual(del_resp.status_code, status.HTTP_204_NO_CONTENT)


class CourseCRUDTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='courseuser', password='coursepass')
		url = reverse('token_obtain_pair')
		resp = self.client.post(url, {'username': 'courseuser', 'password': 'coursepass'}, format='json')
		self.token = resp.data['access']
		self.auth = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

	def test_course_crud(self):
		post_data = {
			'course_name': 'Math',
			'course_code': 'MATH101',
			'description': 'Basic Math',
			'credits': 3
		}
		post_resp = self.client.post('/courses/', post_data, format='json', **self.auth)
		self.assertEqual(post_resp.status_code, status.HTTP_201_CREATED)
		course_id = post_resp.data['course_id']

		get_resp = self.client.get('/courses/', **self.auth)
		self.assertEqual(get_resp.status_code, status.HTTP_200_OK)
		self.assertTrue(any(c['course_id'] == course_id for c in get_resp.data))

		detail_resp = self.client.get(f'/courses/{course_id}/', **self.auth)
		self.assertEqual(detail_resp.status_code, status.HTTP_200_OK)
		self.assertEqual(detail_resp.data['course_name'], 'Math')

		put_data = post_data.copy()
		put_data['course_name'] = 'Advanced Math'
		put_resp = self.client.put(f'/courses/{course_id}/', put_data, format='json', **self.auth)
		self.assertEqual(put_resp.status_code, status.HTTP_200_OK)
		self.assertEqual(put_resp.data['course_name'], 'Advanced Math')

		del_resp = self.client.delete(f'/courses/{course_id}/', **self.auth)
		self.assertEqual(del_resp.status_code, status.HTTP_204_NO_CONTENT)


class EnrollmentAndGradeCRUDTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='enrolluser', password='enrollpass')
		url = reverse('token_obtain_pair')
		resp = self.client.post(url, {'username': 'enrolluser', 'password': 'enrollpass'}, format='json')
		self.token = resp.data['access']
		self.auth = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}

		# Create student and course
		s_resp = self.client.post('/students/', {
			'first_name': 'Alice',
			'last_name': 'Smith',
			'email': 'alice.smith@example.com',
			'date_of_birth': '2001-02-02'
		}, format='json', **self.auth)
		self.student_id = s_resp.data['student_id']
		c_resp = self.client.post('/courses/', {
			'course_name': 'Science',
			'course_code': 'SCI101',
			'description': 'Basic Science',
			'credits': 4
		}, format='json', **self.auth)
		self.course_id = c_resp.data['course_id']

	def test_enrollment_and_grade_crud(self):
		# ENROLLMENT CRUD
		enroll_data = {
			'student_id': self.student_id,
			'course_id': self.course_id
		}
		enroll_resp = self.client.post('/enrollments/', enroll_data, format='json', **self.auth)
		self.assertEqual(enroll_resp.status_code, status.HTTP_201_CREATED)
		enrollment_id = enroll_resp.data['enrollment_id']

		get_resp = self.client.get('/enrollments/', **self.auth)
		self.assertEqual(get_resp.status_code, status.HTTP_200_OK)
		self.assertTrue(any(e['enrollment_id'] == enrollment_id for e in get_resp.data))

		detail_resp = self.client.get(f'/enrollments/{enrollment_id}/', **self.auth)
		self.assertEqual(detail_resp.status_code, status.HTTP_200_OK)
		self.assertEqual(detail_resp.data['student_id'], self.student_id)

		# GRADE CRUD
		grade_data = {
			'enrollment_id': enrollment_id,
			'score': 85
		}
		grade_resp = self.client.post('/grades/', grade_data, format='json', **self.auth)
		self.assertEqual(grade_resp.status_code, status.HTTP_201_CREATED)
		grade_id = grade_resp.data['grade_id']

		get_grades = self.client.get('/grades/', **self.auth)
		self.assertEqual(get_grades.status_code, status.HTTP_200_OK)
		self.assertTrue(any(g['grade_id'] == grade_id for g in get_grades.data))

		detail_grade = self.client.get(f'/grades/{grade_id}/', **self.auth)
		self.assertEqual(detail_grade.status_code, status.HTTP_200_OK)
		self.assertEqual(detail_grade.data['score'], 85)

		put_grade = grade_data.copy()
		put_grade['score'] = 90
		put_resp = self.client.put(f'/grades/{grade_id}/', put_grade, format='json', **self.auth)
		self.assertEqual(put_resp.status_code, status.HTTP_200_OK)
		self.assertEqual(put_resp.data['score'], 90)

		del_resp = self.client.delete(f'/grades/{grade_id}/', **self.auth)
		self.assertEqual(del_resp.status_code, status.HTTP_204_NO_CONTENT)
