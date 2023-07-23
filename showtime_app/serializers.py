from rest_framework import serializers
from showtime_app.models import Movie, Venue, Ticket, Review, Order, User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
