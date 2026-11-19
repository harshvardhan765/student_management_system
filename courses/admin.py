from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "course_code",
        "course_name",
        "teacher",
        "credits",
        "is_active",
    )

    list_filter = (
        "is_active",
        "credits",
    )

    search_fields = (
        "course_code",
        "course_name",
        "teacher__employee_id",
        "teacher__user__first_name",
        "teacher__user__last_name",
    )

    ordering = (
        "course_code",
    )