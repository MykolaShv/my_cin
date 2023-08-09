from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import CountryModelForm, FilmModelForm, ActorModelForm, DirectorModelForm, \
    GenreModelForm, GalleryModelForm, CommentModelForm
from .models import Actor, Country, Director, Genre, PhotoGallery, Film, Comment

User = settings.AUTH_USER_MODEL

class AllActors(ListView):
    model = Actor
    template_name = "actors.html"
    context_object_name = 'actors'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('last_name')
        return queryset


class AllCountries(ListView):
    model = Country
    template_name = "countries.html"
    context_object_name = 'countries'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        return queryset


class AllDirectors(ListView):
    model = Director
    template_name = "directors.html"
    context_object_name = 'directors'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('last_name')
        return queryset


class AllGenres(ListView):
    model = Genre
    template_name = "genres.html"
    context_object_name = 'genres'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        return queryset


class AllGalleries(ListView):
    model =  PhotoGallery
    template_name = "galleries.html"
    context_object_name = 'galleries'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('film')
        return queryset


class AllFilms(ListView):
    model =  Film
    template_name = "films.html"
    context_object_name = 'films'

    # def get_queryset(self):
    #     queryset = super().get_queryset().order_by('releases')
    #     return queryset


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'one_actor.html'
    context_object_name = "actor"


class CountryDetailView(DetailView):
    model = Country
    template_name = 'one_country.html'
    context_object_name = "country"


class DirectorDetailView(DetailView):
    model = Director
    template_name = 'one_director.html'
    context_object_name = "director"


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'one_genre.html'
    context_object_name = "genre"


class GalleryDetailView(DetailView):
    model = PhotoGallery
    template_name = 'one_gallery.html'
    context_object_name = "gallery"




class FilmCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = FilmModelForm
    template_name = 'film_create.html'
    login_url = settings.LOGIN_URL
    success_message = "Film %(title)s is created"
    success_url = reverse_lazy('main')


class FilmEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Film
    template_name = 'edit_film.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "film %(title)s is updated"


class FilmDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Film
    context_object_name = 'film'
    template_name = 'film_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "film is deleted"


class TitleFilmsView(ListView):
    model = Film
    template_name = "film_by_name.html"
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('title')
        return queryset


class RatingFilmsView(ListView):
    model = Film
    template_name = "film_by_rating.html"
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('rating').order_by('title')
        return queryset


class ReleaseFilmsView(ListView):
    model = Film
    template_name = "film_by_release.html"
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('releases')
        return queryset



class FilmDetailView(DetailView):
    model = Film
    template_name = 'one_film.html'
    context_object_name = "film"
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(movie=self.object).order_by('created_at')
        context['form'] = CommentModelForm
        return context


class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CommentModelForm
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Comment is created"

    def form_valid(self, form, **kwargs):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.movie = get_object_or_404(Film) #id= self.kwargs.get("int")
        self.obj.save()
        return super().form_valid(form=form)

# class CommentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#     model = Comment
#     template_name = 'comment_edit.html'
#     fields = 'text'
#     success_url = reverse_lazy('main')
#     login_url = settings.LOGIN_URL
#     success_message = "Yor comment is updated"
#
# class CommentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
#     model = Comment
#     context_object_name = 'post'
#     template_name = 'comment_delete.html'
#     success_url = reverse_lazy('main')
#     login_url = '/login/'
#     success_message = "Comment is deleted"


class CountryCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CountryModelForm
    template_name = 'country_create.html'
    login_url = settings.LOGIN_URL
    success_message = "Country %(name)s is created"
    success_url = reverse_lazy('main')


class CountryEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Country
    template_name = 'edit_country.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "country %(name)s is updated"


class CountryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Country
    context_object_name = 'country'
    template_name = 'country_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Country is deleted"


class CountryFilmsView(ListView):
    model = Film
    template_name = "film_by_country.html"
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('country')
        return queryset


class ActorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = ActorModelForm
    template_name = 'actor_create.html'
    login_url = settings.LOGIN_URL
    success_message = "Actor %(first_name)s %(last_name)s  is created"
    success_url = reverse_lazy('main')


class ActorEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Actor
    template_name = 'edit_actor.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Actor %(first_name)s %(last_name)s  is created is updated"


class ActorDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Actor
    context_object_name = 'actor'
    template_name = 'actor_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Actor is deleted"


class ActorFilmsView(ListView):
    model = Film
    template_name = "film_by_actor.html"
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('actors')
        return queryset


class DirectorCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = DirectorModelForm
    template_name = 'director_create.html'
    login_url = settings.LOGIN_URL
    success_message = "Director %(first_name)s %(last_name)s is created"
    success_url = reverse_lazy('main')


class DirectorEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Director
    template_name = 'edit_director.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "director  %(first_name)s %(last_name)s is updated"


class DirectorDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Director
    context_object_name = 'director'
    template_name = 'director_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Director is deleted"


class DirectorFilmsView(ListView):
    model = Film
    template_name = "film_by_director.html"
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('directors')
        return queryset


class GenreCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = GenreModelForm
    template_name = 'genre_create.html'
    login_url = settings.LOGIN_URL
    success_message = "Genre %(name)s is created"
    success_url = reverse_lazy('main')


class GenreEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Genre
    template_name = 'edit_genre.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Genre %(name)s is updated"


class GenreDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Genre
    context_object_name = 'genre'
    template_name = 'genre_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Genre is deleted"


class GenreFilmsView(ListView):
    model = Film
    template_name = "film_by_genre.html"
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('genres')
        return queryset


class GalleryCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = GalleryModelForm
    template_name = 'gallery_create.html'
    login_url = settings.LOGIN_URL
    success_message = "Gallery %(title)s is created"
    success_url = reverse_lazy('main')


class GalleryEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PhotoGallery
    template_name = 'edit_gallery.html'
    fields = '__all__'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Gallery %(title)s is updated"


class GalleryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PhotoGallery
    context_object_name = 'gallery'
    template_name = 'gallery_delete.html'
    success_url = reverse_lazy('main')
    login_url = settings.LOGIN_URL
    success_message = "Gallery is deleted"


# Create your views here.
