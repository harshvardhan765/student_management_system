from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Course
from .forms import CourseForm


@login_required
def course_list(request):

    courses = Course.objects.select_related(
        "teacher",
        "teacher__user"
    )

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses
        }
    )


@login_required
def add_course(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Course added successfully!"
            )

            return redirect("course_list")

    else:

        form = CourseForm()

    return render(
        request,
        "courses/add_course.html",
        {
            "form": form
        }
    )


@login_required
def edit_course(request, pk):

    course = get_object_or_404(
        Course,
        pk=pk
    )

    if request.method == "POST":

        form = CourseForm(
            request.POST,
            instance=course
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Course updated successfully!"
            )

            return redirect("course_list")

    else:

        form = CourseForm(
            instance=course
        )

    return render(
        request,
        "courses/add_course.html",
        {
            "form": form
        }
    )


@login_required
def delete_course(request, pk):

    course = get_object_or_404(
        Course,
        pk=pk
    )

    if request.method == "POST":

        course.delete()

        messages.success(
            request,
            "Course deleted successfully!"
        )

        return redirect("course_list")

    return render(
        request,
        "courses/delete_course.html",
        {
            "course": course
        }
    )