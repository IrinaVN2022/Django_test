from django import forms

from students.models import Student
from groups.models import Group


class GroupBaseForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=None, required=False)

    def save(self, commit=True):
        new_group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = new_group
            student.save()

    class Meta:
        model = Group
        fields = [
            'title',
            'start_date',
            'description',
            'headman',
            'teachers',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }


class CreateGroupForm(GroupBaseForm):
    # students = forms.ModelMultipleChoiceField(queryset=Student.objects.filter(group__isnull=True))
    """
        FROM student where group is null
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(group__isnull=True).select_related('group')

    class Meta(GroupBaseForm.Meta):
        pass


class UpdateGroupForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(group__isnull=True).select_related('group')

    class Meta (GroupBaseForm.Meta):
        exclude = [
            'start_date'
        ]
