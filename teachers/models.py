from django.db import models
from django.conf import settings


class Teacher(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="teacher_profile"
    )

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    subject = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=150
    )

    experience = models.PositiveIntegerField(
        default=0,
        help_text="Experience in years"
    )

    joining_date = models.DateField()

    profile_picture = models.ImageField(
        upload_to="teachers/",
        blank=True,
        null=True
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
        ordering = ["employee_id"]

    def __str__(self):
        full_name = self.user.get_full_name()

        if full_name:
            return f"{full_name} ({self.employee_id})"

        return f"{self.user.username} ({self.employee_id})"
    