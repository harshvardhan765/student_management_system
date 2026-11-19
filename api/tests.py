import json
from datetime import date
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from courses.models import Course
from teachers.models import Teacher
from students.models import Student
from attendance.models import Attendance

User = get_user_model()


class APITestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_api_home(self):
        response = self.client.get("/api/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["status"])
        self.assertIn("endpoints", data)

    def test_course_crud(self):
        # Create course
        payload = {
            "course_code": "PHY101",
            "course_name": "Physics I",
            "credits": 3,
            "description": "Introductory physics",
        }
        res = self.client.post("/api/courses/", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res.status_code, 201)
        course_id = res.json()["data"]["id"]

        # Fetch course
        res = self.client.get(f"/api/courses/{course_id}")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["data"]["course_code"], "PHY101")

        # Update course
        res = self.client.put(f"/api/courses/{course_id}", data=json.dumps({"course_name": "Physics Mechanics"}), content_type="application/json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["data"]["course_name"], "Physics Mechanics")

        # Delete course
        res = self.client.delete(f"/api/courses/{course_id}")
        self.assertEqual(res.status_code, 200)

    def test_teacher_crud(self):
        payload = {
            "username": "teacher_bob",
            "first_name": "Bob",
            "last_name": "Taylor",
            "email": "bob.taylor@test.com",
            "password": "Password123!",
            "employee_id": "TCH-001",
            "phone": "9876543210",
            "subject": "Mathematics",
            "qualification": "M.Sc Mathematics",
            "experience": 4,
            "joining_date": "2021-01-10",
        }
        res = self.client.post("/api/teachers/", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res.status_code, 201)
        teacher_id = res.json()["data"]["id"]

        res = self.client.get(f"/api/teachers/{teacher_id}")
        self.assertEqual(res.status_code, 200)

        res = self.client.put(f"/api/teachers/{teacher_id}", data=json.dumps({"experience": 5}), content_type="application/json")
        self.assertEqual(res.status_code, 200)

        res = self.client.delete(f"/api/teachers/{teacher_id}")
        self.assertEqual(res.status_code, 200)

    def test_student_crud(self):
        # Create student
        payload = {
            "username": "charlie_test",
            "first_name": "Charlie",
            "last_name": "Brown",
            "email": "charlie@test.com",
            "password": "Password123!",
            "roll_number": "STU-001",
            "phone": "5551112222",
            "gender": "Male",
            "date_of_birth": "2003-04-12",
            "address": "456 Oak Ave",
        }
        res = self.client.post("/api/students/", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res.status_code, 201)
        student_id = res.json()["data"]["id"]

        # Duplicate roll number error
        res_dup = self.client.post("/api/students/", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(res_dup.status_code, 422)
        self.assertFalse(res_dup.json()["status"])

        # Fetch student
        res = self.client.get(f"/api/students/{student_id}")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["data"]["roll_number"], "STU-001")

        # Update student
        res = self.client.put(
            f"/api/students/{student_id}",
            data=json.dumps({"first_name": "Charles", "address": "999 Pine Rd"}),
            content_type="application/json"
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["data"]["first_name"], "Charles")
        self.assertEqual(res.json()["data"]["address"], "999 Pine Rd")

        # Delete student
        res = self.client.delete(f"/api/students/{student_id}")
        self.assertEqual(res.status_code, 200)
