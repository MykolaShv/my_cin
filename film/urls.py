from django.urls import path

from .views import CountryCreate, GalleryCreate, GenreCreate, DirectorCreate, ActorCreate, FilmCreate, \
    AllActors, AllCountries, AllDirectors, AllGenres, AllGalleries, ActorDetailView, CountryDetailView, \
    DirectorDetailView, GenreDetailView, GalleryDetailView, GalleryDeleteView, GenreDeleteView, DirectorDeleteView, \
    ActorDeleteView, CountryDeleteView, CountryEditView, ActorEditView, DirectorEditView, GenreEditView, \
    GalleryEditView, AllFilms, FilmDetailView, FilmDeleteView, FilmEditView, TitleFilmsView, CountryFilmsView, \
    CommentCreateView, ActorFilmsView, DirectorFilmsView, GenreFilmsView, RatingFilmsView, ReleaseFilmsView

urlpatterns = [
    path('all_actors/', AllActors.as_view(), name='all_actors'),
    path('all_countries/', AllCountries.as_view(), name='all_countries'),
    path('all_directors/', AllDirectors.as_view(), name='all_directors'),
    path('all_genres/', AllGenres.as_view(), name='all_genres'),
    path('all_galleries/', AllGalleries.as_view(), name='all_galleries'),
    path('all_films/', AllFilms.as_view(), name='all_films'),
    path('actor_detail/<int:pk>/', ActorDetailView.as_view(), name='actor_detail'),
    path('country_detail/<int:pk>/',CountryDetailView.as_view(), name='country_detail'),
    path('director_detail/<int:pk>/',DirectorDetailView.as_view(), name='director_detail'),
    path('genre_detail/<int:pk>/',GenreDetailView.as_view(), name='genre_detail'),
    path('gallery_detail/<int:pk>/',GalleryDetailView.as_view(), name='gallery_detail'),
    path('film_detail/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('film_create/', FilmCreate.as_view(), name = 'film_create'),
    path('film/<int:pk>/delete/', FilmDeleteView.as_view(), name='film_delete'),
    path('film/<int:pk>/edit/', FilmEditView.as_view(), name='film_edit'),
    path('film_by_title/',TitleFilmsView.as_view(), name='film_by_title'),
    path('film_rating/', RatingFilmsView.as_view(), name='film_rating'),
    path('film_release/', ReleaseFilmsView.as_view(), name='film_release'),
    path('<int:pk>/create_comment/', CommentCreateView.as_view(), name='create_comment'),
    path('country_create/', CountryCreate.as_view(), name = 'country_create'),
    path('by_country/<int:pk>/delete/', CountryDeleteView.as_view(), name='country_delete'),
    path('by_country/<int:pk>/edit/', CountryEditView.as_view(), name='country_edit'),
    path('by_country/',  CountryFilmsView.as_view(), name = 'by_country'),
    path('actor_create/', ActorCreate.as_view(), name='actor_create'),
    path('by_actor/<int:pk>/delete/', ActorDeleteView.as_view(), name='actor_delete'),
    path('by_actor/<int:pk>/edit/', ActorEditView.as_view(), name='actor_edit'),
    path('by_actor/', ActorFilmsView.as_view(), name = 'by_actor'),
    path('director_create/', DirectorCreate.as_view(), name='director_create'),
    path('by_director/<int:pk>/delete/', DirectorDeleteView.as_view(), name='director_delete'),
    path('by_director/<int:pk>/edit/', DirectorEditView.as_view(), name='director_edit'),
    path('by_director/',  DirectorFilmsView.as_view(), name = 'by_director'),
    path('genre_create/', GenreCreate.as_view(), name='genre_create'),
    path('by_genre/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre_delete'),
    path('by_genre/<int:pk>/edit/', GenreEditView.as_view(), name='genre_edit'),
    path('by_genre/',  GenreFilmsView.as_view(), name = 'by_genre'),
    path('create_gallery/', GalleryCreate.as_view(), name='create_gallery'),
    path('delete_gallery/<int:pk>/', GalleryDeleteView.as_view(), name='delete_gallery'),
    path('edit_gallery/<int:pk>/', GalleryEditView.as_view(), name='edit_gallery'),
]
