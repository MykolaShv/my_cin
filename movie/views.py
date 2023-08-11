from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .forms import CreateHallForm, ReleaseForm, SessionForm
from .models import Session, Hall, Release
import os, sys
from django.conf import settings


#  робота із залом
class CreateHallView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_staff'
    model = Hall
    form_class = CreateHallForm
    success_url = reverse_lazy('main')
    template_name = 'create_hall.html'
    login_url = settings.LOGIN_URL


class HallEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Hall
    template_name = 'edit_hall.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "hall %(name)s is updated"


class HallListView(ListView):
    model = Hall
    template_name = 'hall_list.html'
    context_object_name = 'halls'


class HallDetailView(PermissionRequiredMixin, DetailView):
    login_url = settings.LOGIN_URL
    permission_required = 'is_staff'
    model = Hall
    template_name = 'hall_detail.html'
    context_object_name = "hall"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        hall = Hall.objects.get(id=self.object.id)
        rows = hall.rows
        cols = hall.cols

        context = {
            'name': hall.name,
            'rows': [number for number in range(1, rows + 1)],
            'cols': [number for number in range(1, cols + 1)],
            'photo': hall.photo
        }
        return context


class HallDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Hall
    context_object_name = 'hall'
    template_name = 'hall_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Hall is deleted"


# робота із сесіями
class CreateSessionView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_staff'
    model = Session
    form_class = SessionForm
    success_url = reverse_lazy('main')
    template_name = 'create_session.html'
    login_url = settings.LOGIN_URL


class SessionEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Session
    template_name = 'edit_session.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Session %(movie)s is updated"


class SessionListView(ListView):
    model = Session
    template_name = 'session_list.html'
    context_object_name = 'sessions'


class SessionDetailView(PermissionRequiredMixin, DetailView):
    login_url = settings.LOGIN_URL
    permission_required = 'is_staff'
    model = Session
    template_name = 'session_detail.html'
    context_object_name = "session"


class SessionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Session
    context_object_name = 'session'
    template_name = 'session_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "session is deleted"


# робота фільму в прокаті
class CreateReleaseView(PermissionRequiredMixin, CreateView):
    permission_required = 'is_staff'
    model = Release
    form_class = ReleaseForm
    success_url = reverse_lazy('main')
    template_name = 'create_release.html'
    login_url = settings.LOGIN_URL


class ReleaseEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Release
    template_name = 'edit_release.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Release %(movie)s is updated"


class ReleaseListView(ListView):
    model = Release
    template_name = 'release_list.html'
    context_object_name = 'releases'


class ReleaseDetailView(PermissionRequiredMixin, DetailView):
    login_url = settings.LOGIN_URL
    permission_required = 'is_staff'
    model = Release
    template_name = 'release_detail.html'
    context_object_name = "release"


class ReleaseDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Release
    context_object_name = 'release'
    template_name = 'release_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Release is deleted"


# інтуїція каже що потрібно щось з квитками робити - але ЩО? поки не розумію
def buy_ticket(request):
    return HttpResponse("Hey! It's your buy_ticket view!!")


def ticket_detail(request):
    return HttpResponse("Hey! It's your ticket_detail view!!")


def ticket_list(request):
    return HttpResponse("Hey! It's your ticket_list view!!")


def ticket_create(request):
    return HttpResponse("Hey! It's your ticket_create view!!")


def print_ticket(request):
    return HttpResponse("Hey! It's your print_ticket view!!")


#  скоріше видалю - бо там потрібно просто створити фільтр  фільмів
def soon_list(request):
    return HttpResponse("Hey! It's your soon_list view!!")


# початкове, потім в кінці виведо , що хочу і що є  на екран, пуста сторінка
class MainListView(ListView):
    model = Session
    template_name = "main.html"


# поки не впевнений чи потрібно - може просто прописати в головному про кінотеатра
def about(request):
    return HttpResponse("Hey! It's your about view!!")


# не впевнений чи потрібно, скоріше видалю
def session_search(request):
    return HttpResponse("Hey! It's your session_search view!!")
