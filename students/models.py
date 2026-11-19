from django.db import models
from django.conf import settings
from courses.models import Course


class Student(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    roll_number = models.CharField(
        max_length=20,
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    address = models.TextField()

    admission_date = models.DateField(
        auto_now_add=True
    )

    profile_picture = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    
    class Meta:
        ordering = ["roll_number"]

    def __str__(self):
        full_name = self.user.get_full_name()

        if full_name:
            return f"{full_name} ({self.roll_number})"

        return f"{self.user.username} ({self.roll_number})"
    