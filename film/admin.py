from django.contrib import admin
from .models import Country, Actor, Director, Genre, Film, PhotoGallery, Comment


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ('name',)

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'birth_date', 'description', 'photo')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'birth_date', 'description', 'photo')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ('name',)

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'poster', 'country', 'directors', 'actors', 'genres',
              'running_time', 'trailer', 'rating', 'age_rating')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'film')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('text', 'movie', 'author')

    def create_date(self, obj):
        return obj.created

    create_date.empty_value_display = '???'
