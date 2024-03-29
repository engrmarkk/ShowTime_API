from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from showtime_app.models import Movie
from showtime_app.serializers import MovieSerializer


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = (IsAuthenticated,)


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminUser)

    def get_object(self):
        title = self.kwargs.get('title')
        return get_object_or_404(Movie, title=title)


class MovieGenreList(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        genre = self.kwargs.get('genre')
        return Movie.objects.filter(genres=genre)


class GetMovieByCode(APIView):
    serializer_class = MovieSerializer

    def get(self, request, code):
        movie = get_object_or_404(Movie, movie_code=code)
        serializer = self.serializer_class(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

