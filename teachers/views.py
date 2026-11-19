from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model

from .models import Teacher
from .forms import TeacherForm

User = get_user_model()


@login_required
def teacher_list(request):

    teachers = Teacher.objects.select_related("user")

    return render(
        request,
        "teachers/teacher_list.html",
        {
            "teachers": teachers
        }
    )


@login_required
def add_teacher(request):

    if request.method == "POST":

        form = TeacherForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                role="teacher",
            )

            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()

            messages.success(
                request,
                "Teacher added successfully!"
            )

            return redirect("teacher_list")

    else:

        form = TeacherForm()

    return render(
        request,
        "teachers/add_teacher.html",
        {
            "form": form
        }
    )


@login_required
def edit_teacher(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    if request.method == "POST":

        form = TeacherForm(
            request.POST,
            request.FILES,
            instance=teacher
        )

        if form.is_valid():

            user = teacher.user

            user.username = form.cleaned_data["username"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.email = form.cleaned_data["email"]

            password = form.cleaned_data["password"]

            if password:
                user.set_password(password)

            user.save()

            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()

            messages.success(
                request,
                "Teacher updated successfully!"
            )

            return redirect(
                "teacher_list"
            )

    else:

        form = TeacherForm(
            instance=teacher
        )

    return render(
        request,
        "teachers/add_teacher.html",
        {
            "form": form
        }
    )


@login_required
def delete_teacher(request, pk):

    teacher = get_object_or_404(
        Teacher,
        pk=pk
    )

    if request.method == "POST":

        teacher.user.delete()

        messages.success(
            request,
            "Teacher deleted successfully!"
        )

        return redirect(
            "teacher_list"
        )

    return render(
        request,
        "teachers/delete_teacher.html",
        {
            "teacher": teacher
        }
    )