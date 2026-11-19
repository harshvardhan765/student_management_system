from http import HTTPStatus
import logging

from django.contrib.auth import get_user_model
from django.db import transaction
from ninja import Router
from ninja.errors import HttpError

from courses.models import Course
from students.models import Student

from .schemas import (
    StudentSchema,
    StudentCreateSchema,
    StudentUpdateSchema,
    StudentResponseSchema,
    StudentListResponseSchema,
    MessageSchema,
    ErrorResponseSchema,
)

logger = logging.getLogger(__name__)
User = get_user_model()

router = Router(tags=["Student"])


# ==========================================
# Helper Function
# ==========================================

def student_to_dict(student: Student) -> dict:
    return {
        "id": student.id,
        "username": student.user.username,
        "first_name": student.user.first_name,
        "last_name": student.user.last_name,
        "email": student.user.email,
        "roll_number": student.roll_number,
        "phone": student.phone,
        "gender": student.gender,
        "date_of_birth": student.date_of_birth,
        "address": student.address,
        "course_id": student.course.id if student.course else None,
        "course_name": student.course.course_name if student.course else None,
        "is_active": student.is_active,
    }


# ==========================================
# GET ALL STUDENTS
# ==========================================

@router.get(
    "",
    response={
        HTTPStatus.OK: StudentListResponseSchema,
    },
    summary="Get All Students",
    description="Retrieve a list of all students.",
)
def get_students(request):
    students = (
        Student.objects
        .select_related("user", "course")
        .order_by("id")
    )

    return HTTPStatus.OK, {
        "status": True,
        "message": "Students fetched successfully.",
        "data": [
            student_to_dict(student)
            for student in students
        ],
    }


# ==========================================
# GET STUDENT BY ID
# ==========================================

@router.get(
    "/{student_id}",
    response={
        HTTPStatus.OK: StudentResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Get Student By ID",
    description="Retrieve a single student using their ID.",
)
def get_student(request, student_id: int):
    student = (
        Student.objects
        .select_related("user", "course")
        .filter(id=student_id)
        .first()
    )

    if not student:
        raise HttpError(
            HTTPStatus.NOT_FOUND,
            "Student not found."
        )

    return HTTPStatus.OK, {
        "status": True,
        "message": "Student fetched successfully.",
        "data": student_to_dict(student),
    }


# ==========================================
# POST / CREATE STUDENT
# ==========================================

@router.post(
    "",
    response={
        HTTPStatus.CREATED: StudentResponseSchema,
        HTTPStatus.UNPROCESSABLE_ENTITY: ErrorResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
        HTTPStatus.INTERNAL_SERVER_ERROR: ErrorResponseSchema,
    },
    summary="Create Student",
    description="Create a new student and their linked user account.",
)
def create_student(request, payload: StudentCreateSchema):
    try:
        with transaction.atomic():
            if User.objects.filter(username=payload.username).exists():
                return HTTPStatus.UNPROCESSABLE_ENTITY, {
                    "status": False,
                    "message": "Username already exists."
                }

            if User.objects.filter(email=payload.email).exists():
                return HTTPStatus.UNPROCESSABLE_ENTITY, {
                    "status": False,
                    "message": "Email already exists."
                }

            if Student.objects.filter(roll_number=payload.roll_number).exists():
                return HTTPStatus.UNPROCESSABLE_ENTITY, {
                    "status": False,
                    "message": "Roll number already exists."
                }

            course = None
            if payload.course_id:
                course = Course.objects.filter(id=payload.course_id).first()
                if not course:
                    return HTTPStatus.NOT_FOUND, {
                        "status": False,
                        "message": "Course not found."
                    }

            user_obj = User.objects.create_user(
                username=payload.username,
                first_name=payload.first_name,
                last_name=payload.last_name,
                email=payload.email,
                password=payload.password,
                role="student",
            )

            student = Student.objects.create(
                user=user_obj,
                roll_number=payload.roll_number,
                phone=payload.phone,
                gender=payload.gender,
                date_of_birth=payload.date_of_birth,
                address=payload.address,
                course=course,
            )

            return HTTPStatus.CREATED, {
                "status": True,
                "message": "Student created successfully.",
                "data": student_to_dict(student)
            }

    except Exception as e:
        logger.exception("Error while creating student")
        return HTTPStatus.INTERNAL_SERVER_ERROR, {
            "status": False,
            "message": "Something went wrong while creating the student."
        }


# ==========================================
# PUT / UPDATE STUDENT
# ==========================================

@router.put(
    "/{student_id}",
    response={
        HTTPStatus.OK: StudentResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
        HTTPStatus.UNPROCESSABLE_ENTITY: ErrorResponseSchema,
        HTTPStatus.INTERNAL_SERVER_ERROR: ErrorResponseSchema,
    },
    summary="Update Student",
    description="Update an existing student's details.",
)
def update_student(request, student_id: int, payload: StudentUpdateSchema):
    try:
        with transaction.atomic():
            student = (
                Student.objects.select_related("user", "course")
                .filter(id=student_id)
                .first()
            )

            if not student:
                raise HttpError(HTTPStatus.NOT_FOUND, "Student not found.")

            # Email uniqueness check
            if payload.email is not None:
                if User.objects.exclude(id=student.user.id).filter(email=payload.email).exists():
                    raise HttpError(
                        HTTPStatus.UNPROCESSABLE_ENTITY, "Email already exists."
                    )
                student.user.email = payload.email

            # Roll number uniqueness check
            if payload.roll_number is not None:
                if Student.objects.exclude(id=student.id).filter(roll_number=payload.roll_number).exists():
                    raise HttpError(
                        HTTPStatus.UNPROCESSABLE_ENTITY, "Roll number already exists."
                    )
                student.roll_number = payload.roll_number

            # Update user fields
            if payload.first_name is not None:
                student.user.first_name = payload.first_name
            if payload.last_name is not None:
                student.user.last_name = payload.last_name
            student.user.save()

            # Course check
            if payload.course_id is not None:
                if payload.course_id == 0:
                    student.course = None
                else:
                    course = Course.objects.filter(id=payload.course_id).first()
                    if not course:
                        raise HttpError(HTTPStatus.NOT_FOUND, "Course not found.")
                    student.course = course

            # Update student profile fields
            if payload.phone is not None:
                student.phone = payload.phone
            if payload.gender is not None:
                student.gender = payload.gender
            if payload.date_of_birth is not None:
                student.date_of_birth = payload.date_of_birth
            if payload.address is not None:
                student.address = payload.address
            if payload.is_active is not None:
                student.is_active = payload.is_active

            student.save()

            return HTTPStatus.OK, {
                "status": True,
                "message": "Student updated successfully.",
                "data": student_to_dict(student),
            }

    except HttpError:
        raise
    except Exception as e:
        logger.error(f"Unexpected error during student update: {e}", exc_info=True)
        return HTTPStatus.INTERNAL_SERVER_ERROR, {
            "status": False,
            "message": "Something went wrong while updating the student."
        }


# ==========================================
# DELETE STUDENT
# ==========================================

@router.delete(
    "/{student_id}",
    response={
        HTTPStatus.OK: MessageSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Delete Student",
    description="Delete a student and their linked user account.",
)
def delete_student(request, student_id: int):
    student = Student.objects.select_related("user").filter(id=student_id).first()

    if not student:
        return HTTPStatus.NOT_FOUND, {
            "status": False,
            "message": "Student not found."
        }

    user = student.user
    student.delete()
    if user:
        user.delete()

    return HTTPStatus.OK, {
        "status": True,
        "message": "Student deleted successfully."
    }
