from http import HTTPStatus
import logging

from ninja import Router
from ninja.errors import HttpError

from attendance.models import Attendance
from students.models import Student
from courses.models import Course

from .schemas import (
    AttendanceSchema,
    AttendanceCreateSchema,
    AttendanceResponseSchema,
    AttendanceListResponseSchema,
    MessageSchema,
    ErrorResponseSchema,
)

logger = logging.getLogger(__name__)

router = Router(tags=["Attendance"])


def attendance_to_dict(att: Attendance) -> dict:
    return {
        "id": att.id,
        "student_id": att.student.id,
        "student_name": att.student.user.get_full_name() or att.student.user.username,
        "course_id": att.course.id,
        "course_name": att.course.course_name,
        "date": att.date,
        "status": att.status,
        "remarks": att.remarks or "",
    }


@router.get(
    "",
    response={HTTPStatus.OK: AttendanceListResponseSchema},
    summary="Get All Attendance Records",
)
def get_attendance(request):
    records = Attendance.objects.select_related("student__user", "course").order_by("-date", "id")
    return HTTPStatus.OK, {
        "status": True,
        "message": "Attendance records fetched successfully.",
        "data": [attendance_to_dict(r) for r in records],
    }


@router.get(
    "/{record_id}",
    response={
        HTTPStatus.OK: AttendanceResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Get Attendance Record By ID",
)
def get_attendance_record(request, record_id: int):
    record = Attendance.objects.select_related("student__user", "course").filter(id=record_id).first()
    if not record:
        raise HttpError(HTTPStatus.NOT_FOUND, "Attendance record not found.")

    return HTTPStatus.OK, {
        "status": True,
        "message": "Attendance record fetched successfully.",
        "data": attendance_to_dict(record),
    }


@router.post(
    "",
    response={
        HTTPStatus.CREATED: AttendanceResponseSchema,
        HTTPStatus.UNPROCESSABLE_ENTITY: ErrorResponseSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Mark Attendance",
)
def mark_attendance(request, payload: AttendanceCreateSchema):
    student = Student.objects.filter(id=payload.student_id).first()
    if not student:
        return HTTPStatus.NOT_FOUND, {
            "status": False,
            "message": "Student not found."
        }

    course = Course.objects.filter(id=payload.course_id).first()
    if not course:
        return HTTPStatus.NOT_FOUND, {
            "status": False,
            "message": "Course not found."
        }

    if Attendance.objects.filter(student=student, course=course, date=payload.date).exists():
        return HTTPStatus.UNPROCESSABLE_ENTITY, {
            "status": False,
            "message": "Attendance record for this student and course on this date already exists."
        }

    record = Attendance.objects.create(
        student=student,
        course=course,
        date=payload.date,
        status=payload.status,
        remarks=payload.remarks,
    )

    return HTTPStatus.CREATED, {
        "status": True,
        "message": "Attendance marked successfully.",
        "data": attendance_to_dict(record),
    }


@router.delete(
    "/{record_id}",
    response={
        HTTPStatus.OK: MessageSchema,
        HTTPStatus.NOT_FOUND: ErrorResponseSchema,
    },
    summary="Delete Attendance Record",
)
def delete_attendance(request, record_id: int):
    record = Attendance.objects.filter(id=record_id).first()
    if not record:
        return HTTPStatus.NOT_FOUND, {
            "status": False,
            "message": "Attendance record not found."
        }

    record.delete()
    return HTTPStatus.OK, {
        "status": True,
        "message": "Attendance record deleted successfully."
    }
