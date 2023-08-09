from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _
from film.models import Film
from django.conf import settings

User = settings.AUTH_USER_MODEL

months = [_('January'), _('February'), _('March'), _('April'), _('May'), _('June'), _('July'),
          _('August'), _('September'), _('October'), _('November'), _('December')]


class Hall(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Hall name'))
    rows = models.IntegerField()
    seats = models.IntegerField()
    photo = models.ImageField(upload_to='img/others/', blank=True, null=True)

    def capacity(self):
        return self.rows * self.seats

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Hall')
        verbose_name_plural = _('Halls')


class Release(models.Model):
    class Meta:
        verbose_name = _('Release')
        verbose_name_plural = _('Releases')
        ordering = ["start_date"]

    movie = models.ForeignKey(Film, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name=_('Start date'))
    end_date = models.DateField(verbose_name=_('End date'))

    def __str__(self):
        return self.movie.title + " " + str(self.start_date)

class ScheduleDay(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    day = models.IntegerField(blank=False, null=False)  # день тижня, пн - 1, вівт - 2 тощо
    start_at = models.TimeField(blank=True, null=True)  # не знаю як прописати декілька стартів, НЕВЖЕ створювати
    #                                                    новий клас і через ForeignKey обирати?
    release = models.ForeignKey(Release, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Release"))

    def __str__(self):
        return str(self.release.movie) + " " + str(self.hall) + " " + str(self.day) + " " + str(self.start_at)

    class Meta:
        verbose_name = _('ScheduleDay')


class Session(models.Model):
    class Meta:
        verbose_name = _('Session')

    one_session = models.ForeignKey(ScheduleDay, on_delete=models.CASCADE, verbose_name=_('One session'))
    price = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_('Ticket price'))


class Seat(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    row = models.IntegerField()
    seat = models.IntegerField()

    class Meta:
        unique_together = ('row', 'seat')


class Ticket(models.Model):
    spectator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name=_("Spectator"),
                                  related_name="movie_spectator_ticket")
    amount = models.PositiveSmallIntegerField(verbose_name=_("Session"), validators=[MinValueValidator(1),
                                                                                     MaxValueValidator(1000)])
    time_purchase = models.DateTimeField(auto_now=True)
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING, verbose_name=_("Session"),
                                related_name="session")
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")
        ordering = ["time_purchase"]

# Create your models here.
