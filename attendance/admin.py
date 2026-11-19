from django.contrib import admin

from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "course",
        "date",
        "status",
    )

    list_filter = (
        "status",
        "course",
        "date",
    )

    search_fields = (
        "student__user__first_name",
        "student__user__last_name",
        "student__roll_number",
        "course__course_code",
        "course__course_name",
    )

    ordering = (
        "-date",
    )