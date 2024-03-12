from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Course


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'
