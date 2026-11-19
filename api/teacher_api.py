from http import HTTPStatus
import logging

from django.contrib.auth import get_user_model
from django.db import transaction
from ninja import Router
from ninja.errors import HttpError

from teachers.models import Teacher

from .schemas import (
    TeacherSchema,
    TeacherCreateSchema,
    TeacherUpdateSchema,
    TeacherResponseSchema,
    TeacherListResponseSchema,
    MessageSchema,
    ErrorResponseSchema,
)

logger = logging.getLogger(__name__)
User = get_user_model()

router = Router(tags=["Teacher"])


def teacher_to_dict(teacher: Teacher) -> dict:
    return {
        "id": teacher.id,
        "username": teacher.user.username,
        "first_name": teacher.user.first_name,
        "last_name": teacher.user.last_name,
        "email": teacher.user.email,
        "employee_id": teacher.employee_id,
        "phone": teacher.phone,
        "subject": teacher.subject,
        "qualification": teacher.qualification,
        "experience": teacher.experience,
        "joining_date": teacher.joining_date,
        "is_active": teacher.is_active,
    }


@router.get(
    "",
    response={HTTPStatus.OK: TeacherListResponseSchema},
    summary="Get All Teachers",
)
def get_teachers(request):
    teachers = Teacher.objects.select_related("user").order_by("employee_id")
    return HTTPStatus.OK, {
        "status": True,
        "message": "Teachers fetched successfully.",
        "data": [teacher_to_dict(t) for t in teachers],
    }


@router.get(
    "/{teacher_id}",
    response={
        HTTPStatus.OK: TeacherResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Get Teacher By ID",
)
def get_teacher(request, teacher_id: int):
    teacher = Teacher.objects.select_related("user").filter(id=teacher_id).first()
    if not teacher:
        raise HttpError(HTTPStatus.NOT_FOUND, "Teacher not found.")

    return HTTPStatus.OK, {
        "status": True,
        "message": "Teacher fetched successfully.",
        "data": teacher_to_dict(teacher),
    }


@router.post(
    "",
    response={
        HTTPStatus.CREATED: TeacherResponseSchema,
        HTTPStatus.UNPROCESSABLE_ENTITY: ErrorResponseSchema,
        HTTPStatus.INTERNAL_SERVER_ERROR: ErrorResponseSchema,
    },
    summary="Create Teacher",
)
def create_teacher(request, payload: TeacherCreateSchema):
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

            if Teacher.objects.filter(employee_id=payload.employee_id).exists():
                return HTTPStatus.UNPROCESSABLE_ENTITY, {
                    "status": False,
                    "message": "Employee ID already exists."
                }

            user = User.objects.create_user(
                username=payload.username,
                first_name=payload.first_name,
                last_name=payload.last_name,
                email=payload.email,
                password=payload.password,
                role="teacher",
            )

            teacher = Teacher.objects.create(
                user=user,
                employee_id=payload.employee_id,
                phone=payload.phone,
                subject=payload.subject,
                qualification=payload.qualification,
                experience=payload.experience,
                joining_date=payload.joining_date,
            )

            return HTTPStatus.CREATED, {
                "status": True,
                "message": "Teacher created successfully.",
                "data": teacher_to_dict(teacher),
            }

    except Exception as e:
        logger.exception("Error while creating teacher")
        return HTTPStatus.INTERNAL_SERVER_ERROR, {
            "status": False,
            "message": "Something went wrong while creating the teacher."
        }


@router.put(
    "/{teacher_id}",
    response={
        HTTPStatus.OK: TeacherResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
        HTTPStatus.UNPROCESSABLE_ENTITY: ErrorResponseSchema,
    },
    summary="Update Teacher",
)
def update_teacher(request, teacher_id: int, payload: TeacherUpdateSchema):
    teacher = Teacher.objects.select_related("user").filter(id=teacher_id).first()
    if not teacher:
        raise HttpError(HTTPStatus.NOT_FOUND, "Teacher not found.")

    with transaction.atomic():
        if payload.email is not None:
            if User.objects.exclude(id=teacher.user.id).filter(email=payload.email).exists():
                raise HttpError(HTTPStatus.UNPROCESSABLE_ENTITY, "Email already exists.")
            teacher.user.email = payload.email

        if payload.employee_id is not None:
            if Teacher.objects.exclude(id=teacher.id).filter(employee_id=payload.employee_id).exists():
                raise HttpError(HTTPStatus.UNPROCESSABLE_ENTITY, "Employee ID already exists.")
            teacher.employee_id = payload.employee_id

        if payload.first_name is not None:
            teacher.user.first_name = payload.first_name
        if payload.last_name is not None:
            teacher.user.last_name = payload.last_name
        teacher.user.save()

        if payload.phone is not None:
            teacher.phone = payload.phone
        if payload.subject is not None:
            teacher.subject = payload.subject
        if payload.qualification is not None:
            teacher.qualification = payload.qualification
        if payload.experience is not None:
            teacher.experience = payload.experience
        if payload.joining_date is not None:
            teacher.joining_date = payload.joining_date
        if payload.is_active is not None:
            teacher.is_active = payload.is_active

        teacher.save()

    return HTTPStatus.OK, {
        "status": True,
        "message": "Teacher updated successfully.",
        "data": teacher_to_dict(teacher),
    }


@router.delete(
    "/{teacher_id}",
    response={
        HTTPStatus.OK: MessageSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Delete Teacher",
)
def delete_teacher(request, teacher_id: int):
    teacher = Teacher.objects.select_related("user").filter(id=teacher_id).first()
    if not teacher:
        return HTTPStatus.NOT_FOUND, {
            "status": False,
            "message": "Teacher not found."
        }

    user = teacher.user
    teacher.delete()
    if user:
        user.delete()

    return HTTPStatus.OK, {
        "status": True,
        "message": "Teacher deleted successfully."
    }
