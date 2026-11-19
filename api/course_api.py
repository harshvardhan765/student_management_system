from http import HTTPStatus
import logging

from ninja import Router
from ninja.errors import HttpError

from courses.models import Course
from teachers.models import Teacher

from .schemas import (
    CourseSchema,
    CourseCreateSchema,
    CourseUpdateSchema,
    CourseResponseSchema,
    CourseListResponseSchema,
    MessageSchema,
    ErrorResponseSchema,
)

logger = logging.getLogger(__name__)

router = Router(tags=["Course"])


def course_to_dict(course: Course) -> dict:
    return {
        "id": course.id,
        "course_code": course.course_code,
        "course_name": course.course_name,
        "credits": course.credits,
        "description": course.description or "",
        "is_active": course.is_active,
        "teacher_id": course.teacher.id if course.teacher else None,
        "teacher_name": str(course.teacher) if course.teacher else None,
    }


@router.get(
    "",
    response={HTTPStatus.OK: CourseListResponseSchema},
    summary="Get All Courses",
)
def get_courses(request):
    courses = Course.objects.select_related("teacher", "teacher__user").order_by("course_code")
    return HTTPStatus.OK, {
        "status": True,
        "message": "Courses fetched successfully.",
        "data": [course_to_dict(c) for c in courses],
    }


@router.get(
    "/{course_id}",
    response={
        HTTPStatus.OK: CourseResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Get Course By ID",
)
def get_course(request, course_id: int):
    course = Course.objects.select_related("teacher", "teacher__user").filter(id=course_id).first()
    if not course:
        raise HttpError(HTTPStatus.NOT_FOUND, "Course not found.")

    return HTTPStatus.OK, {
        "status": True,
        "message": "Course fetched successfully.",
        "data": course_to_dict(course),
    }


@router.post(
    "",
    response={
        HTTPStatus.CREATED: CourseResponseSchema,
        HTTPStatus.UNPROCESSABLE_ENTITY: ErrorResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Create Course",
)
def create_course(request, payload: CourseCreateSchema):
    code = payload.course_code.upper().strip()
    if Course.objects.filter(course_code=code).exists():
        return HTTPStatus.UNPROCESSABLE_ENTITY, {
            "status": False,
            "message": "Course code already exists."
        }

    teacher = None
    if payload.teacher_id:
        teacher = Teacher.objects.filter(id=payload.teacher_id).first()
        if not teacher:
            return HTTPStatus.NOT_FOUND, {
                "status": False,
                "message": "Teacher not found."
            }

    course = Course.objects.create(
        course_code=code,
        course_name=payload.course_name.strip(),
        credits=payload.credits,
        description=payload.description.strip(),
        teacher=teacher,
        is_active=payload.is_active,
    )

    return HTTPStatus.CREATED, {
        "status": True,
        "message": "Course created successfully.",
        "data": course_to_dict(course),
    }


@router.put(
    "/{course_id}",
    response={
        HTTPStatus.OK: CourseResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
        HTTPStatus.UNPROCESSABLE_ENTITY: ErrorResponseSchema,
    },
    summary="Update Course",
)
def update_course(request, course_id: int, payload: CourseUpdateSchema):
    course = Course.objects.filter(id=course_id).first()
    if not course:
        raise HttpError(HTTPStatus.NOT_FOUND, "Course not found.")

    if payload.course_code is not None:
        code = payload.course_code.upper().strip()
        if Course.objects.exclude(id=course.id).filter(course_code=code).exists():
            raise HttpError(HTTPStatus.UNPROCESSABLE_ENTITY, "Course code already exists.")
        course.course_code = code

    if payload.course_name is not None:
        course.course_name = payload.course_name.strip()
    if payload.credits is not None:
        course.credits = payload.credits
    if payload.description is not None:
        course.description = payload.description.strip()
    if payload.is_active is not None:
        course.is_active = payload.is_active

    if payload.teacher_id is not None:
        if payload.teacher_id == 0:
            course.teacher = None
        else:
            teacher = Teacher.objects.filter(id=payload.teacher_id).first()
            if not teacher:
                raise HttpError(HTTPStatus.NOT_FOUND, "Teacher not found.")
            course.teacher = teacher

    course.save()

    return HTTPStatus.OK, {
        "status": True,
        "message": "Course updated successfully.",
        "data": course_to_dict(course),
    }


@router.delete(
    "/{course_id}",
    response={
        HTTPStatus.OK: MessageSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Delete Course",
)
def delete_course(request, course_id: int):
    course = Course.objects.filter(id=course_id).first()
    if not course:
        return HTTPStatus.NOT_FOUND, {
            "status": False,
            "message": "Course not found."
        }

    course.delete()
    return HTTPStatus.OK, {
        "status": True,
        "message": "Course deleted successfully."
    }
