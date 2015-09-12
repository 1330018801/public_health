# coding=utf-8
from django.forms import ModelForm
from .models import EducationActivity


class EducationActivityForm(ModelForm):
    class Meta:
        model = EducationActivity
        fields = '__all__'