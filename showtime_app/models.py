from django.db import models
from django.contrib.auth.models import User


class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    performers = models.CharField(max_length=200)
    genres = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()


class Ticket(models.Model):
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()


class Review(models.Model):
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    rating = models.PositiveIntegerField()
    comment = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
