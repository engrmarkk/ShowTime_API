from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


def get_ticket_types():
    return [
        ('regular', 'Regular'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP'),
    ]


def get_genres():
    return [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
        ('thriller', 'Thriller'),
    ]


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255, default="", blank=True)
    lastname = models.CharField(max_length=255, default="", blank=True)
    phone = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genres = models.CharField(max_length=100, choices=get_genres(), default='action')
    movie_code = models.CharField(max_length=10)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50, choices=get_ticket_types(), default='regular')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.ticket_type


class Review(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50, default='Anonymous')
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.user_name


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50, choices=get_ticket_types())
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user
