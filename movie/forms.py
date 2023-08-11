from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Hall, Release, Session
from django import forms


class CreateHallForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Hall
        fields = '__all__'


class SessionForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Session
        fields = '__all__'


class ReleaseForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Release
        fields = '__all__'
