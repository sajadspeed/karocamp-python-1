from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "name",
            "phone",
            "std_number",
            "bio",
            "age",
            "is_married",
        ]
