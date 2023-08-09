from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django import forms
from .models import Country, Actor, Director, Genre, Film, PhotoGallery, Comment

User = settings.AUTH_USER_MODEL


class CountryModelForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Country
        fields = ('name',)


class ActorModelForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'birth_date', 'description', 'photo')


class DirectorModelForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Director
        fields = ('first_name', 'last_name', 'birth_date', 'description', 'photo')


class GenreModelForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Genre
        fields = ('name',)


class FilmModelForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Film
        fields = ('title', 'description', 'poster', 'country', 'directors', 'actors',
                  'genres', 'running_time',  'trailer', 'rating', 'age_rating')


class GalleryModelForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = PhotoGallery
        fields = ('title', 'photo', 'film')


class CommentModelForm(forms.ModelForm, LoginRequiredMixin):
    class Meta:
        model = Comment
        fields = ['text']


