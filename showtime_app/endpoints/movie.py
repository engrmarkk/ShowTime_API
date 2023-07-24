from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from showtime_app.models import Movie, Venue, Ticket, Review, Order, User
from showtime_app.serializers import MovieSerializer


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = (IsAuthenticated,)


class MovieDetail(generics.RetrieveAPIView):
    serializer_class = MovieSerializer

    def get_object(self):
        title = self.kwargs.get('title')
        movie = get_object_or_404(Movie, title=title)
        return movie
