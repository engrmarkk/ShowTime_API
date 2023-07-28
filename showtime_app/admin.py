from django.contrib import admin
from .models import Movie, Ticket, Venue, Review, Order, CustomUser

# Register your models here.
admin.site.register(Movie)
admin.site.register(Ticket)
admin.site.register(Venue)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(CustomUser)
