from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Country(models.Model):
    name = models.CharField("Country", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Actor(models.Model):
    first_name = models.CharField(verbose_name="First_name", max_length=255)
    last_name = models.CharField(verbose_name="last_name", max_length=255)
    birth_date = models.DateField(verbose_name="Birth_date", blank=True, null=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    photo = models.ImageField(blank=True, verbose_name="Picture", upload_to="img/actors/")  # потрібна папка

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"


class Director(models.Model):
    first_name = models.CharField(verbose_name="First_name", max_length=255)
    last_name = models.CharField(verbose_name="Last_name", max_length=255)
    birth_date = models.DateField(verbose_name="Birth_date", blank=True, null=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    photo = models.ImageField(blank=True, verbose_name="Picture", upload_to="img/directors/")  # потрібна папка

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"


class Genre(models.Model):
    name = models.CharField("Name", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Film(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    description = models.TextField(verbose_name="Description")
    poster = models.ImageField(verbose_name="Posters", upload_to="img/movies/")
    country = models.ManyToManyField(Country, verbose_name="Countries")
    directors = models.ManyToManyField(Director, verbose_name="Director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Actors", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="Genres")
    running_time = models.PositiveSmallIntegerField("Running time", blank=True, null=True)
    trailer = models.URLField(blank=True, default='')
    RATING = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10))
    rating = models.IntegerField(choices=RATING, blank=False)

    AGERATING = ((1, "21+"), (2, "18+"), (3, "16+"), (4, "12+"), (5, "6+"))
    age_rating = models.IntegerField(choices=AGERATING, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"


class PhotoGallery(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    photo = models.ImageField(blank=True, verbose_name="Image", upload_to="img/film_shots/")
    film = models.ForeignKey(Film, verbose_name="Film", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Photo gallery"
        verbose_name_plural = "Photo gallery"


class Comment(models.Model):  # було Rewiew
    text = models.TextField("Comment", max_length=5000)
    movie = models.ForeignKey(Film, verbose_name="film", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return f"{self.movie}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
