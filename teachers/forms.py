from django import forms
from django.contrib.auth import get_user_model

from .models import Teacher

User = get_user_model()


class TeacherForm(forms.ModelForm):

    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = Teacher

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "employee_id",
            "phone",
            "subject",
            "qualification",
            "experience",
            "joining_date",
            "profile_picture",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if self.instance.pk:

            self.fields["username"].initial = self.instance.user.username
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["email"].initial = self.instance.user.email

            self.fields["password"].help_text = (
                "Leave blank to keep the current password."
            )

    def clean_username(self):

        username = self.cleaned_data["username"]

        qs = User.objects.filter(username=username)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.user.pk)

        if qs.exists():
            raise forms.ValidationError("Username already exists.")

        return username

    def clean_email(self):

        email = self.cleaned_data["email"]

        qs = User.objects.filter(email=email)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.user.pk)

        if qs.exists():
            raise forms.ValidationError("Email already exists.")

        return email

    def clean_employee_id(self):

        employee_id = self.cleaned_data["employee_id"]

        qs = Teacher.objects.filter(employee_id=employee_id)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError(
                "Employee ID already exists."
            )

        return employee_id