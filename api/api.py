from http import HTTPStatus

from ninja import NinjaAPI
from ninja.errors import HttpError

from .student_api import router as student_router
from .course_api import router as course_router
from .teacher_api import router as teacher_router
from .attendance_api import router as attendance_router


api = NinjaAPI(
    title="Student Management System API",
    version="1.0.0",
    description="REST APIs for Student Management System",
    docs_url="/docs",
)


# ==============================
# Global Exception Handler
# ==============================

@api.exception_handler(HttpError)
def http_error_handler(request, exc):
    return api.create_response(
        request,
        {
            "status": False,
            "message": str(exc),
        },
        status=exc.status_code,
    )


# ==============================
# Home
# ==============================

@api.get(
    "/",
    tags=["Home"],
    summary="API Home",
)
def api_home(request):
    return {
        "status": True,
        "message": "Welcome to Student Management System API",
        "endpoints": {
            "docs": "/api/docs",
            "students": "/api/students/",
            "courses": "/api/courses/",
            "teachers": "/api/teachers/",
            "attendance": "/api/attendance/",
        }
    }


# ==============================
# Routers
# ==============================

api.add_router("/students/", student_router, tags=["Student"])
api.add_router("/courses/", course_router, tags=["Course"])
api.add_router("/teachers/", teacher_router, tags=["Teacher"])
api.add_router("/attendance/", attendance_router, tags=["Attendance"])
