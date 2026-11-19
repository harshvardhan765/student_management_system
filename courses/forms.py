from django import forms

from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = [
            "course_code",
            "course_name",
            "teacher",
            "credits",
            "description",
            "is_active",
        ]

        widgets = {
            "course_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Course Code",
                }
            ),

            "course_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Course Name",
                }
            ),

            "teacher": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "credits": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Enter Course Description",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def clean_course_code(self):

        course_code = self.cleaned_data["course_code"].upper()

        qs = Course.objects.filter(course_code=course_code)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError(
                "Course Code already exists."
            )

        return course_code