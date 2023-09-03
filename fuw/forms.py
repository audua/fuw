from django import forms
from fuw.models import Student


class PlaceholderMixin(forms.Form):
    _special_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in self._special_fields:
                field.widget.attrs['placeholder'] = f"{field.label}*" if field.required else field.label
                field.label = False


class StudentForm(PlaceholderMixin, forms.Form):
    matric_number = forms.CharField(max_length=20, required=True, label='Matric Number')



