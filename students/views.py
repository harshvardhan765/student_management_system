import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model

from .forms import StudentForm
from .models import Student
from teachers.models import Teacher
from courses.models import Course
from attendance.models import Attendance

User = get_user_model()


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):

    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    course_count = Course.objects.count()
    attendance_count = Attendance.objects.count()

    course_data = (
        Course.objects
        .annotate(total_students=Count("students"))
        .values("course_name", "total_students")
    )

    course_labels = [item["course_name"] for item in course_data]
    course_counts = [item["total_students"] for item in course_data]

    context = {
        "student_count": student_count,
        "teacher_count": teacher_count,
        "course_count": course_count,
        "attendance_count": attendance_count,
        "course_labels": json.dumps(course_labels),
        "course_counts": json.dumps(course_counts),
    }

    return render(request, "dashboard.html", context)


@login_required
def student_list(request):

    search_query = request.GET.get("q", "").strip()

    students = Student.objects.select_related(
        "user",
        "course"
    )

    if search_query:
        students = students.filter(
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query) |
            Q(user__username__icontains=search_query) |
            Q(user__email__icontains=search_query) |
            Q(roll_number__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(course__course_name__icontains=search_query)
        )

    students = students.order_by("roll_number")

    paginator = Paginator(students, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "students/student_list.html",
        {
            "students": page_obj,
            "page_obj": page_obj,
            "search_query": search_query,
        }
    )


@login_required
def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                role="student",
            )

            student = form.save(commit=False)
            student.user = user
            student.save()

            messages.success(
                request,
                "Student added successfully!"
            )

            return redirect("student_list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {
            "form": form
        }
    )


@login_required
def edit_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            user = student.user

            user.username = form.cleaned_data["username"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]

            password = form.cleaned_data["password"]

            if password:
                user.set_password(password)

            user.save()

            student = form.save(commit=False)
            student.user = user
            student.save()

            messages.success(
                request,
                "Student updated successfully!"
            )

            return redirect("student_list")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/add_student.html",
        {
            "form": form
        }
    )


@login_required
def delete_student(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":

        student.user.delete()

        messages.success(
            request,
            "Student deleted successfully!"
        )

        return redirect("student_list")

    return render(
        request,
        "students/delete_student.html",
        {
            "student": student
        }
    )