from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AttendanceForm
from .models import Attendance


@login_required
def attendance_list(request):

    attendance_records = Attendance.objects.select_related(
        "student__user",
        "course",
    )

    return render(
        request,
        "attendance/attendance_list.html",
        {
            "attendance_records": attendance_records,
        },
    )


@login_required
def add_attendance(request):

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Attendance added successfully!",
            )

            return redirect("attendance_list")

    else:

        form = AttendanceForm()

    return render(
        request,
        "attendance/add_attendance.html",
        {
            "form": form,
        },
    )


@login_required
def edit_attendance(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk,
    )

    if request.method == "POST":

        form = AttendanceForm(
            request.POST,
            instance=attendance,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Attendance updated successfully!",
            )

            return redirect("attendance_list")

    else:

        form = AttendanceForm(
            instance=attendance,
        )

    return render(
        request,
        "attendance/add_attendance.html",
        {
            "form": form,
        },
    )


@login_required
def delete_attendance(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk,
    )

    if request.method == "POST":

        attendance.delete()

        messages.success(
            request,
            "Attendance deleted successfully!",
        )

        return redirect("attendance_list")

    return render(
        request,
        "attendance/delete_attendance.html",
        {
            "attendance": attendance,
        },
    )