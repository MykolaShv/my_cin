from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from movie.models import Ticket


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required field')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('superuser must have is_staff = True')

        if not extra_fields.get('is_superuser'):
            raise ValueError('superuser must have is_superuser = True')

        user = self.create_user(email, password, **extra_fields)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=256, blank=False, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    ticket = models.ManyToManyField(Ticket, blank=True)
    city = models.CharField(max_length=200, verbose_name='Town', blank=True)
    date_joined = models.DateTimeField(auto_now=True, blank=True, null=True)  # delete blank and null
    last_login = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profile_image', blank=True, null=True)
    is_staff = models.BooleanField('Is staff user', default=False)
    is_superuser = models.BooleanField('Is admin', default=False)
    is_active = models.BooleanField('Active', default=True)
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'email']

    objects = UserManager()

    def __str__(self):
        return f"{self.username}- {self.name}- {self.id} "

    def get_username(self):
        return f'{self.username}'
