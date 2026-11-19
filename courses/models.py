from django.db import models
from teachers.models import Teacher


class Course(models.Model):

    course_code = models.CharField(
        max_length=20,
        unique=True
    )

    course_name = models.CharField(
        max_length=100
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses"
    )

    credits = models.PositiveIntegerField(
        default=3
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["course_code"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"