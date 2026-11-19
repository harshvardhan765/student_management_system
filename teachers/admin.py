from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = (
        "employee_id",
        "user",
        "subject",
        "phone",
        "qualification",
        "experience",
        "joining_date",
        "is_active",
    )

    list_filter = (
        "subject",
        "qualification",
        "is_active",
    )

    search_fields = (
        "employee_id",
        "user__username",
        "user__first_name",
        "user__last_name",
        "subject",
    )

    ordering = (
        "employee_id",
    )