from datetime import date
from typing import Optional, List
from ninja import Schema


# ==========================================
# Generic Message & Error Schemas
# ==========================================

class MessageSchema(Schema):
    status: bool = True
    message: str


class ErrorResponseSchema(Schema):
    status: bool = False
    message: str


# ==========================================
# Student Schemas
# ==========================================

class StudentSchema(Schema):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str

    roll_number: str
    phone: str
    gender: str

    date_of_birth: date
    address: str

    course_id: Optional[int] = None
    course_name: Optional[str] = None

    is_active: bool


class StudentCreateSchema(Schema):
    username: str
    first_name: str
    last_name: str = ""
    email: str
    password: str

    roll_number: str
    phone: str
    gender: str
    date_of_birth: date
    address: str

    course_id: Optional[int] = None


class StudentUpdateSchema(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    roll_number: Optional[str] = None

    phone: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    address: Optional[str] = None

    course_id: Optional[int] = None
    is_active: Optional[bool] = None


class StudentResponseSchema(Schema):
    status: bool = True
    message: str
    data: StudentSchema


class StudentListResponseSchema(Schema):
    status: bool = True
    message: str
    data: List[StudentSchema]


# ==========================================
# Course Schemas
# ==========================================

class CourseSchema(Schema):
    id: int
    course_code: str
    course_name: str
    credits: int
    description: str
    is_active: bool
    teacher_id: Optional[int] = None
    teacher_name: Optional[str] = None


class CourseCreateSchema(Schema):
    course_code: str
    course_name: str
    credits: int = 3
    description: str = ""
    teacher_id: Optional[int] = None
    is_active: bool = True


class CourseUpdateSchema(Schema):
    course_code: Optional[str] = None
    course_name: Optional[str] = None
    credits: Optional[int] = None
    description: Optional[str] = None
    teacher_id: Optional[int] = None
    is_active: Optional[bool] = None


class CourseResponseSchema(Schema):
    status: bool = True
    message: str
    data: CourseSchema


class CourseListResponseSchema(Schema):
    status: bool = True
    message: str
    data: List[CourseSchema]


# ==========================================
# Teacher Schemas
# ==========================================

class TeacherSchema(Schema):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    employee_id: str
    phone: str
    subject: str
    qualification: str
    experience: int
    joining_date: date
    is_active: bool


class TeacherCreateSchema(Schema):
    username: str
    first_name: str
    last_name: str = ""
    email: str
    password: str
    employee_id: str
    phone: str
    subject: str
    qualification: str
    experience: int = 0
    joining_date: date


class TeacherUpdateSchema(Schema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    employee_id: Optional[str] = None
    phone: Optional[str] = None
    subject: Optional[str] = None
    qualification: Optional[str] = None
    experience: Optional[int] = None
    joining_date: Optional[date] = None
    is_active: Optional[bool] = None


class TeacherResponseSchema(Schema):
    status: bool = True
    message: str
    data: TeacherSchema


class TeacherListResponseSchema(Schema):
    status: bool = True
    message: str
    data: List[TeacherSchema]


# ==========================================
# Attendance Schemas
# ==========================================

class AttendanceSchema(Schema):
    id: int
    student_id: int
    student_name: str
    course_id: int
    course_name: str
    date: date
    status: str
    remarks: Optional[str] = None


class AttendanceCreateSchema(Schema):
    student_id: int
    course_id: int
    date: date
    status: str = "Present"
    remarks: Optional[str] = None


class AttendanceResponseSchema(Schema):
    status: bool = True
    message: str
    data: AttendanceSchema


class AttendanceListResponseSchema(Schema):
    status: bool = True
    message: str
    data: List[AttendanceSchema]
