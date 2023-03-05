from django import forms
from django.http import HttpResponse
from django_filters import FilterSet

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'city',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})

        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_phone(self):
        ret = ''
        value = self.cleaned_data.get('phone')
        for elem in value:
            if elem.isdigit():
                ret += elem
            elif elem in '()-+':
                ret += elem
        return ret


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'city',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],  # first_name = 'Alex',   first_name ILIKE '%abc%'
            'last_name': ['exact', 'startswith']  # last_name LIKE 'ABC%'
        }  # AND (OR)
