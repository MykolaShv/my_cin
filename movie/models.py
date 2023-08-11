import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _
from film.models import Film
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Seat(models.Model):
    id = models.AutoField(primary_key=True)
    row = models.PositiveSmallIntegerField(blank=True, null=True)
    col = models.PositiveSmallIntegerField(blank=True, null=True)
    hall = models.ForeignKey('movie.Hall', on_delete=models.CASCADE, related_name='seats')

    class Meta:
        unique_together = ('row', 'col', 'hall')


class Hall(BaseModel):
    id = models.AutoField(primary_key=True)
    rows = models.PositiveSmallIntegerField(blank=True, null=True)
    cols = models.PositiveSmallIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='img/others/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if Hall.objects.filter(name=self.name).first():
            raise ValidationError("This name is already in use!")
        new_hall = self.id is None
        res = super().save(*args, **kwargs)
        if new_hall:
            seats = []
            for row in range(self.rows):
                for col in range(self.cols):
                    seats.append(Seat(row=row + 1, col=col + 1, hall=self))
            Seat.objects.bulk_create(seats)
        return res


class Release(models.Model):
    movie = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name=_('Start date'))
    end_date = models.DateField(verbose_name=_('End date'))

    def __str__(self):
        return self.movie.title + " " + str(self.start_date)

    def save(self, *args, **kwargs):
        if self.end_date < self.start_date:
            raise ValidationError("End date must be after start date.")
        res = super().save(*args, **kwargs)
        return res


class Session(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()
    session = models.ForeignKey(Release, on_delete=models.CASCADE)
    end_next_day = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.session.movie.title + " " + str(self.time_start)

    def save(self, *args, **kwargs):
        if self.time_end < self.time_start:
            raise ValidationError("End date must be after start date.")
        if Session.objects.filter(time_start=self.time_start).first():
            raise ValidationError("for this time the session exists")
        res = super().save(*args, **kwargs)
        return res


class Ticket(models.Model):
    spectator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spectator')
    session_timeframe = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.DO_NOTHING)

    def validate_seats(self):
        if Ticket.objects.filter(seat=self.seat).first():
            raise ValidationError("This seat is already taken!")

    def clean(self):
        if not self.session_timeframe.session.hall.seats.filter(id=self.seat.id).exists():
            raise ValidationError({"seat": "Seat does not exist in this session"})

# Create your models here.
