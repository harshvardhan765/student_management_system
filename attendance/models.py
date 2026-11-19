from django.db import models

from students.models import Student
from courses.models import Course


class Attendance(models.Model):

    STATUS_CHOICES = [
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Late", "Late"),
        ("Leave", "Leave"),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )

    # Temporarily change the course field through chatGPT..!

#     course = models.ForeignKey(
#     Course,
#     on_delete=models.CASCADE,
#     related_name="attendance_records",
#     null=True,
#     blank=True,
# )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Present",
    )

    remarks = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-date", "student__user__first_name"]
        unique_together = ("student", "course", "date")

    def __str__(self):
        return (
            f"{self.student.user.get_full_name()} - "
            f"{self.course.course_code} - "
            f"{self.date}"
        )
    