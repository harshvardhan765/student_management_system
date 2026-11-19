from django import forms
from django.contrib.auth import get_user_model

from .models import Student

User = get_user_model()


class StudentForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,
        label="Username"
    )

    first_name = forms.CharField(
        max_length=100,
        label="First Name"
    )

    last_name = forms.CharField(
        max_length=100,
        required=False,
        label="Last Name"
    )

    email = forms.EmailField(
        label="Email Address"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False,
        label="Password"
    )

    class Meta:
        model = Student

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "roll_number",
            "phone",
            "gender",
            "date_of_birth",
            "course",
            "address",
            "profile_picture",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["password"].help_text = (
                "Leave blank if you don't want to change password."
            )

            self.fields["username"].initial = self.instance.user.username
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name
            self.fields["email"].initial = self.instance.user.email

    def clean_username(self):
        username = self.cleaned_data["username"]

        qs = User.objects.filter(username=username)

        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.user.pk)

        if qs.exists():
            raise forms.ValidationError("Username already exists.")

        return username

    def clean_email(self):
        email = self.cleaned_data["email"]

        qs = User.objects.filter(email=email)

        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.user.pk)

        if qs.exists():
            raise forms.ValidationError("Email already exists.")

        return email

    def clean_roll_number(self):
        roll = self.cleaned_data["roll_number"]

        qs = Student.objects.filter(roll_number=roll)

        if self.instance and self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("Roll number already exists.")

        return roll